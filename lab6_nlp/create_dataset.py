"""Dataset is already committed as corpus.json and queries.json; this script validates them."""
import json
with open("corpus.json",encoding="utf-8") as f: docs=json.load(f)
with open("queries.json",encoding="utf-8") as f: queries=json.load(f)
assert len(docs)>=5 and len(queries)>=10
for q in queries:
    if q["doc"] is not None: assert q["evidence"] in docs[q["doc"]]
print("Dataset validated:",len(docs),"documents;",len(queries),"queries")
