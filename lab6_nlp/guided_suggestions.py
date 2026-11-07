"""Recommend FAQ questions for a partial query using TF-IDF or embeddings."""
import argparse
from guided_chatbot import build_bot

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["tfidf", "embedding"], default="tfidf")
    parser.add_argument("--query", default="assignment upload")
    args = parser.parse_args()
    engine = build_bot(args.backend)
    print(f"Backend: {args.backend}\nSuggested questions:")
    for record, score in engine.search(args.query, k=3):
        print(record["question"], f"({score:.3f})")

if __name__ == "__main__":
    main()
