"""Lab 5: Alpha-beta pruning with leaf counter."""
def alphabeta(depth, index, max_turn, scores, target_depth, alpha, beta, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for i in range(2):
            value = max(value, alphabeta(depth+1, index*2+i, False, scores, target_depth, alpha, beta, counter))
            alpha = max(alpha, value)
            if alpha >= beta: break
        return value
    value = float("inf")
    for i in range(2):
        value = min(value, alphabeta(depth+1, index*2+i, True, scores, target_depth, alpha, beta, counter))
        beta = min(beta, value)
        if alpha >= beta: break
    return value

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 3, 5, 2, 9]
    counter = {"leaves": 0}
    value = alphabeta(0, 0, True, scores, 3, float("-inf"), float("inf"), counter)
    print("Alpha-beta value:", value)
    print("Evaluated leaves:", counter["leaves"])
