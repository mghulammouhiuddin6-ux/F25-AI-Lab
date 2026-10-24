"""Lab 3: UCS compared with BFS on the documented weighted extension."""
from collections import deque
import heapq
GRAPH = {
    "A": [("B", 1), ("C", 10)],
    "B": [("D", 4), ("E", 1)],
    "C": [("F", 1), ("G", 2)],  # added C -> G corridor
    "D": [], "E": [("G", 1)], "F": [], "G": []
}
UNWEIGHTED = {u: [v for v, _ in edges] for u, edges in GRAPH.items()}

def bfs(start, goal):
    q = deque([(start, [start])]); seen = {start}
    while q:
        node, path = q.popleft()
        if node == goal: return path
        for nxt in UNWEIGHTED[node]:
            if nxt not in seen:
                seen.add(nxt); q.append((nxt, path + [nxt]))
    return None

def ucs(start, goal):
    pq = [(0, start, [start])]; best = {start: 0}; order = []
    while pq:
        cost, node, path = heapq.heappop(pq)
        if cost != best.get(node): continue
        order.append(node)
        if node == goal: return path, cost, order
        for nxt, weight in GRAPH[node]:
            new_cost = cost + weight
            if new_cost < best.get(nxt, float("inf")):
                best[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt, path + [nxt]))
    return None, float("inf"), order

if __name__ == "__main__":
    bp = bfs("A", "G")
    up, cost, order = ucs("A", "G")
    def sum_cost(path):
        return sum(dict(GRAPH[u])[v] for u, v in zip(path, path[1:]))
    print("BFS path:", bp, "hops:", len(bp)-1, "cost:", sum_cost(bp))
    print("UCS path:", up, "cost:", cost, "independent sum:", sum_cost(up), "processed:", order)
