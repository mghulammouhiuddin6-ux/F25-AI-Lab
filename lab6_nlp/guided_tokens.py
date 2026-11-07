from task1_tokens import SAMPLES, tokenize
for text in SAMPLES:
    ws, words = tokenize(text)
    print(repr(text), "whitespace:", ws, len(ws), "word-like:", words, len(words))
