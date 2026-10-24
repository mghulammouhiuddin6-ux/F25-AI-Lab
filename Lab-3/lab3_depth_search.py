"""Lab 3: depth-limited search and iterative deepening."""
GRAPH = {"A":["B","C"], "B":["D","E"], "C":["F"], "D":[], "E":["G"], "F":[], "G":[]}

def dls(start, goal, limit):
    def visit(node, path, depth):
        if node == goal: return "FOUND", path
        cutoff = False
        if depth < limit:
            for nxt in GRAPH.get(node, []):
                if nxt in path: continue
                status, result = visit(nxt, path + [nxt], depth + 1)
                if status == "FOUND": return status, result
                if status == "CUTOFF": cutoff = True
        else:
            if GRAPH.get(node, []): cutoff = True
        return ("CUTOFF" if cutoff else "FAILURE"), None
    return visit(start, [start], 0)

def iddfs(start, goal, max_depth):
    attempts = []
    for limit in range(max_depth + 1):
        status, path = dls(start, goal, limit)
        attempts.append((limit, status, path))
        if status == "FOUND": return path, attempts
    return None, attempts

if __name__ == "__main__":
    for limit in range(1, 5):
        print(f"DLS limit={limit}: {dls('A','G',limit)}")
    path, attempts = iddfs("A", "G", 4)
    print("IDDFS path:", path, "| attempts:", attempts)
