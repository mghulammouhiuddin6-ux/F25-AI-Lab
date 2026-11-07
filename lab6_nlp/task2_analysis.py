"""Task 2 experiment: chunk strategy counts, overlap and evidence coverage."""
import json
from task2_chunks import make_chunks

def main():
    docs=json.load(open("corpus.json",encoding="utf-8"))
    labels=json.load(open("queries.json",encoding="utf-8"))
    print("strategy, chunks, avg_words, duplicate_word_units")
    for strategy in ["0","10","sentence"]:
        chunks=make_chunks(docs,strategy)
        total=sum(len(c["text"].split()) for c in chunks)
        original=sum(len(t.split()) for t in docs.values())
        avg=total/len(chunks) if chunks else 0
        print(f"{strategy}, {len(chunks)}, {avg:.2f}, {total-original}")
        for q in labels:
            if q["doc"]:
                preserved=any(c["doc"]==q["doc"] and q["evidence"] in c["text"] for c in chunks)
                print("  evidence",q["doc"],q["split"],"preserved:",preserved)
if __name__=="__main__": main()
