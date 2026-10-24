"""Lab 5: Minimax with terminal-leaf evaluation counter."""
def minimax(depth, index, max_turn, scores, target_depth, counter):
    if depth == target_depth:
        counter["leaves"] += 1
        return scores[index]
    left = minimax(depth+1, index*2, not max_turn, scores, target_depth, counter)
    right = minimax(depth+1, index*2+1, not max_turn, scores, target_depth, counter)
    return max(left, right) if max_turn else min(left, right)

if __name__ == "__main__":
    scores = [3, 5, 2, 9, 3, 5, 2, 9]
    counter = {"leaves": 0}
    value = minimax(0, 0, True, scores, 3, counter)
    print("Minimax value:", value)
    print("Evaluated leaves:", counter["leaves"])
