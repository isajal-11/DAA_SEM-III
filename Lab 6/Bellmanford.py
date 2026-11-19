#0/1 Knapsack problem
V = 5
edges = [
    (0, 1, 6),
    (0, 2, 7),
    (1, 2, 8),
    (1, 3, 5),
    (1, 4, -4),
    (2, 3, -3),
    (2, 4, 9),
    (3, 1, -2),
    (4, 0, 2),
    (4, 3, 7)
]
src = 0

dist = [float('inf')] * V
dist[src] = 0

for i in range(V - 1):
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

negative = False
for u, v, w in edges:
    if dist[u] != float('inf') and dist[u] + w < dist[v]:
        negative = True
        break

if negative:
    print("Negative cycle present")
else:
    for i in range(V):
        print(src, "->", i, ":", dist[i])