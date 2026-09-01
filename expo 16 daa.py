def graph_coloring(graph, num_colors):
    """
    graph format: adjacency list {node_index: [neighbors]}
    """
    n = len(graph)
    colors = [0] * n

    def is_valid(node, color):
        for neighbor in graph[node]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node == n:
            return True

        for c in range(1, num_colors + 1):
            if is_valid(node, c):
                colors[node] = c
                if backtrack(node + 1):
                    return True
                colors[node] = 0

        return False

    if backtrack(0):
        return colors
    return "No solution exists"

# Graph with 4 nodes
graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]}
colors = graph_coloring(graph, num_colors=3)
print("Color assignment per node:", colors)
