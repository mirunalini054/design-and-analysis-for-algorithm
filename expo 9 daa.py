def floyd_warshall_general(matrix):
    """
    Computes all-pairs shortest paths and transitive closure.
    Accepts infinity representations as float('inf').
    """
    n = len(matrix)
    dist = [row[:] for row in matrix]
    reach = [[True if cell < float('inf') else False for cell in row] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Floyd-Warshall (Distance)
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                # Warshall (Transitive Closure / Reachability)
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return dist, reach

INF = float('inf')
graph = [
    [0, 3, INF, 7],
    [8, 0, 2, INF],
    [5, INF, 0, 1],
    [2, INF, INF, 0]
]
distances, reachability = floyd_warshall_general(graph)
print("Shortest Path Matrix:\n", distances)
