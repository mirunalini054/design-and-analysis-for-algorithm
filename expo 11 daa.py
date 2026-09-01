import heapq

def dijkstra_general(graph, source):
    """
    Generic Dijkstra implementation returning shortest distances and path pointers.
    Graph format: {node: [(neighbor, weight), ...]}
    """
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[source] = 0
    
    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        if curr_dist > distances[u]:
            continue

        for neighbor, weight in graph.get(u, []):
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = u
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous

graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 1), ('D', 5)],
    'C': [('D', 8), ('E', 10)],
    'D': [('E', 2)],
    'E': []
}
dist, prev = dijkstra_general(graph, source='A')
print("Shortest Distances:", dist)
