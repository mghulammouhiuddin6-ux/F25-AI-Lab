"""Task 1: compare whitespace and Unicode word-like tokenization."""
import re
import sys
SAMPLES = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "یہ ایک مثال ہے",
]
def tokenize(text: str):
    whitespace = text.split()
    word_like = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    return whitespace, word_like

def main():
    # Keep the Urdu example printable in Windows terminals using legacy encodings.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="backslashreplace")
    print("TASK 1 — TOKENIZATION COMPARISON")
    for number, text in enumerate(SAMPLES, 1):
        ws, words = tokenize(text)
        print(f"\nInput {number}: {text!r}")
        print(f"Whitespace ({len(ws)}): {ws}")
        print(f"Word-like ({len(words)}): {words}")
    print("\nInterpretation: whitespace splitting keeps punctuation attached; the regex extracts word-like runs.")
    print("Risk: punctuation, apostrophes, email structure and Urdu token boundaries may be lost or split.")
    print("The regex is a simple comparison, not a complete multilingual tokenizer.")
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        print("\nModel subword tokenization (observed locally):")
        for text in SAMPLES[:2]:
            print(repr(text), model.tokenizer.tokenize(text))
    except ImportError:
        print("\nOptional model tokenizer skipped: install sentence-transformers to run this comparison.")
    except Exception as exc:
        print(f"\nOptional model tokenizer unavailable: {type(exc).__name__}: {exc}")
if __name__ == "__main__": main()
