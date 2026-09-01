import heapq

def prim(graph, start_node):
    """
    graph format: {u: [(weight, v), ...]}
    """
    mst = []
    visited = {start_node}
    edges = [(w, start_node, v) for w, v in graph[start_node]]
    heapq.heapify(edges)
    total_weight = 0

    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            total_weight += w

            for next_w, neighbor in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(edges, (next_w, v, neighbor))

    return mst, total_weight

graph = {
    'A': [(1, 'B'), (3, 'C')],
    'B': [(1, 'A'), (3, 'C'), (6, 'D')],
    'C': [(3, 'A'), (3, 'B'), (4, 'D'), (2, 'E')],
    'D': [(6, 'B'), (4, 'C'), (5, 'E')],
    'E': [(2, 'C'), (5, 'D')]
}
mst_edges, weight = prim(graph, 'A')
print(f"Prim MST Edges: {mst_edges}, Total Weight: {weight}")
