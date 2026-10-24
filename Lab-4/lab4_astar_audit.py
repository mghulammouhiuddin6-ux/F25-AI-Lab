"""Lab 4: A*, UCS control, expansion trace, and heuristic overestimate experiment."""
import heapq
GRAPH = {"S":[("A",1),("B",4)], "A":[("C",2)], "B":[("G",5)], "C":[("G",3)], "G":[]}
H = {"S":5, "A":4, "B":4, "C":2, "G":0}

def search(heuristic):
    pq = [(heuristic["S"], 0, "S", ["S"])]
    best = {"S": 0}; expanded = []; processed = []
    while pq:
        f, g, node, path = heapq.heappop(pq)
        if g != best.get(node): continue
        processed.append((node, g, heuristic[node], f))
        if node == "G": return path, g, expanded, processed
        expanded.append(node)  # count only nodes whose successors are examined
        for nxt, w in GRAPH[node]:
            ng = g + w
            if ng < best.get(nxt, float("inf")):
                best[nxt] = ng
                heapq.heappush(pq, (ng + heuristic[nxt], ng, nxt, path + [nxt]))
    return None, float("inf"), expanded, processed

def path_cost(path):
    return sum(dict(GRAPH[u])[v] for u, v in zip(path, path[1:]))

if __name__ == "__main__":
    for label, h in [("A*", H), ("UCS", {n:0 for n in H}),
                     ("Overestimate h(C)=10", {**H, "C":10})]:
        path, cost, expanded, trace = search(h)
        print(f"{label}: path={path}, returned_cost={cost}, verified_cost={path_cost(path)}, expanded={expanded}, count={len(expanded)}")
        print("trace (node,g,h,f):", trace)
