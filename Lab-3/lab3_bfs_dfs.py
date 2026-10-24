"""Lab 3: BFS and DFS traces on the manual's original graph."""
from collections import deque
GRAPH = {"A":["B","C"], "B":["D","E"], "C":["F"], "D":[], "E":["G"], "F":[], "G":[]}

def bfs(start, goal):
    q = deque([(start, [start])]); seen = {start}; order = []
    while q:
        node, path = q.popleft(); order.append(node)
        if node == goal: return path, order
        for nxt in GRAPH.get(node, []):
            if nxt not in seen:
                seen.add(nxt); q.append((nxt, path + [nxt]))
    return None, order

def dfs(start, goal):
    stack = [(start, [start])]; seen = set(); order = []
    while stack:
        node, path = stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node)
        if node == goal: return path, order
        for nxt in reversed(GRAPH.get(node, [])):
            if nxt not in seen: stack.append((nxt, path + [nxt]))
    return None, order

if __name__ == "__main__":
    for name, fn in [("BFS", bfs), ("DFS", dfs)]:
        path, order = fn("A", "G")
        print(f"{name}: path={path}; visit_order={order}")
