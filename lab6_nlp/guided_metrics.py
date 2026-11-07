from task3_retrieval import metrics
rankings=[["a","b","c"],["c","a","b"],["x","y","z"]]
relevant=[{"a"},{"a"},{"a"}]
hit,mrr=metrics(rankings,relevant)
print(f"Hit@3={hit:.3f}; MRR@3={mrr:.3f}")
assert abs(hit-2/3)<1e-9 and abs(mrr-.5)<1e-9
