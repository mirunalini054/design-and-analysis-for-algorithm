def bellman_ford_general(num_vertices, edge_list, source):
    """
    General Bellman-Ford for graphs with negative weights.
    edge_list format: [(u, v, weight), ...]
    """
    dist = {i: float('inf') for i in range(num_vertices)}
    parent = {i: None for i in range(num_vertices)}
    dist[source] = 0

    for _ in range(num_vertices - 1):
        for u, v, w in edge_list:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u

    # Check for negative cycles
    for u, v, w in edge_list:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative weight cycle accessible from source")

    return dist, parent

edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
distances, parents = bellman_ford_general(num_vertices=4, edge_list=edges, source=0)
print("Distances from source 0:", distances)
