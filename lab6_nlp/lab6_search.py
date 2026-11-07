"""Traceable TF-IDF / sentence-embedding retrieval helper for Lab 6."""
from __future__ import annotations
from typing import Iterable
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

class Retriever:
    def __init__(self, records: list[dict], backend: str = "tfidf", model_name: str = "sentence-transformers/all-MiniLM-L6-v2", model=None):
        if not records or any(not isinstance(r.get("text"), str) or not r["text"].strip() for r in records):
            raise ValueError("Provide at least one record with nonempty text")
        if backend not in {"tfidf", "embedding"}:
            raise ValueError("backend must be 'tfidf' or 'embedding'")
        self.records, self.backend = records, backend
        texts = [r["text"] for r in records]
        if backend == "tfidf":
            self.vectorizer = TfidfVectorizer()
            self.matrix = self.vectorizer.fit_transform(texts)
        else:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise RuntimeError("Install sentence-transformers to use --backend embedding") from exc
            self.model = model if model is not None else SentenceTransformer(model_name, device="cpu")
            self.check_length(texts)
            self.matrix = self.model.encode(texts, normalize_embeddings=True, convert_to_numpy=True)

    def check_length(self, texts: Iterable[str]) -> None:
        if self.backend != "embedding":
            return
        for text in texts:
            count = len(self.model.tokenizer(text, truncation=False)["input_ids"])
            if count > self.model.max_seq_length:
                raise ValueError(f"Input has {count} model tokens; limit is {self.model.max_seq_length}. Rechunk it.")

    def search(self, query: str, k: int = 3, filters: dict | None = None):
        if not isinstance(query, str) or not query.strip() or k <= 0:
            return []
        if self.backend == "tfidf":
            q = self.vectorizer.transform([query])
            if q.nnz == 0:
                return []
            scores = (q @ self.matrix.T).toarray()[0]
        else:
            self.check_length([query])
            q = self.model.encode([query], normalize_embeddings=True, convert_to_numpy=True)[0]
            scores = self.matrix @ q
        allowed = [i for i, rec in enumerate(self.records)
                   if all(rec.get(key) == value for key, value in (filters or {}).items())]
        ranked = sorted(allowed, key=lambda i: (-float(scores[i]), i))
        return [(self.records[i], float(scores[i])) for i in ranked[:k]]

def show_hits(hits):
    if not hits:
        print("No matching records.")
    for record, score in hits:
        print(f"{record.get('id','?')} score={score:.3f} source={record.get('source', record.get('doc','unknown'))}")
        print(record["text"])
