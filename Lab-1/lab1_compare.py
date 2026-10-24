"""Lab 1: Compare transparent rules with a probability threshold.
Run: python lab1_compare.py
The probability values are synthetic demonstration inputs; no model is trained.
"""
def symbolic(score, documents_complete, eligibility_confirmed, identity_verified):
    """Return Review only when all explicit policy conditions pass."""
    return "Review" if (
        documents_complete
        and score >= 70
        and eligibility_confirmed
        and identity_verified
    ) else "Hold"

def threshold(probability):
    """A simple illustrative threshold, not a trained or validated classifier."""
    return "Review" if probability >= 0.70 else "Hold"

cases = [
    {"name": "pass", "score": 82, "complete": True, "eligible": True, "verified": True, "prob": 0.81},
    {"name": "eligibility_failure", "score": 82, "complete": True, "eligible": False, "verified": True, "prob": 0.81},
    {"name": "identity_failure", "score": 82, "complete": True, "eligible": True, "verified": False, "prob": 0.81},
    {"name": "threshold_boundary", "score": 70, "complete": True, "eligible": True, "verified": True, "prob": 0.70},
]
print("case | expected_rule | actual_rule | probability_result | reason")
for c in cases:
    actual = symbolic(c["score"], c["complete"], c["eligible"], c["verified"])
    expected = "Review" if c["name"] in {"pass", "threshold_boundary"} else "Hold"
    reason = {
        "pass": "all explicit conditions pass",
        "eligibility_failure": "eligibility condition is false",
        "identity_failure": "identity verification condition is false",
        "threshold_boundary": "score and probability equal their inclusive thresholds",
    }[c["name"]]
    print(f'{c["name"]} | {expected} | {actual} | {threshold(c["prob"])} | {reason}')
