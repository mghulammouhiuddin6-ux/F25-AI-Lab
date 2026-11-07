"""Controlled retrieval evaluation: 3 chunkers x TF-IDF and real sentence embeddings."""
import csv, json, time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks
from lab6_search import Retriever

def metrics(rankings, relevant):
    hits, reciprocal = [], []
    for ids, good in zip(rankings, relevant):
        ranks = [rank for rank, chunk_id in enumerate(ids[:3], 1) if chunk_id in good]
        hits.append(bool(ranks))
        reciprocal.append(1 / ranks[0] if ranks else 0.0)
    return (sum(hits) / len(hits), sum(reciprocal) / len(reciprocal)) if hits else (None, None)

def main():
    with open("corpus.json", encoding="utf-8") as f: docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f: items = json.load(f)
    assert len(docs) >= 5 and len(items) >= 10
    assert sum(q["doc"] is not None and q["split"] == "dev" for q in items) == 4
    assert sum(q["doc"] is not None and q["split"] == "test" for q in items) == 4
    assert sum(q["doc"] is None for q in items) >= 2
    for q in items:
        assert q["split"] in {"dev", "test"}
        if q["doc"] is not None: assert q["evidence"] in docs[q["doc"]]

    model = None
    model_load_seconds = None
    try:
        from sentence_transformers import SentenceTransformer
        started = time.perf_counter()
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        model_load_seconds = time.perf_counter() - started
        print(f"Embedding model load seconds={model_load_seconds:.6f}")
    except Exception as exc:
        print(f"EMBEDDING BACKEND UNAVAILABLE: {type(exc).__name__}: {exc}")
        print("Only TF-IDF configurations can be evaluated in this environment; install requirements and rerun for embeddings.")

    query_texts = [q["query"] for q in items]
    logs = []
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]
        for backend in ["tfidf", "embedding"]:
            if backend == "embedding" and model is None:
                print(f"SKIPPED {strategy}/embedding: sentence-transformers model unavailable")
                continue
            started = time.perf_counter()
            engine = Retriever(chunks, backend, model=model) if backend == "embedding" else Retriever(chunks, backend)
            index_encode_seconds = time.perf_counter() - started
            if backend == "embedding":
                lengths = [len(model.tokenizer(x, truncation=False)["input_ids"]) for x in texts + query_texts]
                print(f"Model token audit {strategy}: max={max(lengths)} limit={model.max_seq_length}")
                if max(lengths) > model.max_seq_length:
                    raise ValueError("Model input limit exceeded; rechunk or shorten input")
            started = time.perf_counter()
            all_hits = [engine.search(q, k=3) for q in query_texts]
            search_seconds = time.perf_counter() - started
            for split in ["dev", "test"]:
                indices = [i for i, q in enumerate(items) if q["split"] == split and q["doc"] is not None]
                rankings, relevant = [], []
                for i in indices:
                    rankings.append([r["id"] for r, score in all_hits[i]])
                    relevant.append({c["id"] for c in chunks if c["doc"] == items[i]["doc"] and items[i]["evidence"] in c["text"]})
                hit, mrr = metrics(rankings, relevant)
                print(f"{strategy}/{backend}/{split}: Hit@3={hit:.3f} MRR@3={mrr:.3f} chunks={len(chunks)} index_encode_seconds={index_encode_seconds:.6f} search_seconds={search_seconds:.6f}")
            for q, hits in zip(items, all_hits):
                for rank, (record, score) in enumerate(hits, 1):
                    logs.append({"strategy": strategy, "backend": backend, "query": q["query"], "split": q["split"], "answerable": q["doc"] is not None, "rank": rank, "score": f"{score:.6f}", "chunk_id": record["id"], "doc": record["doc"], "source": record["source"], "start": record["start"], "end": record["end"], "text": record["text"]})
    if logs:
        with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(logs[0]))
            writer.writeheader(); writer.writerows(logs)
        print(f"Wrote retrieval_log.csv ({len(logs)} ranked rows)")
    else:
        print("No evaluation rows generated; check dependencies.")
    print("Unanswerable queries are logged but excluded from Hit@3/MRR@3; ranked passages are candidates, not verified answers.")

if __name__ == "__main__": main()
