"""Lab 1: scholarship screening rule and probability comparison."""
def rule_based(score, documents_complete, eligibility_confirmed=True, identity_verified=True):
    return "Review" if (
        documents_complete and score >= 70
        and eligibility_confirmed and identity_verified
    ) else "Hold"

def probability_based(probability):
    return "Review" if probability >= 0.70 else "Hold"

if __name__ == "__main__":
    print("Rule-based:", rule_based(76, True, True, True))
    print("Probability threshold:", probability_based(0.76))
