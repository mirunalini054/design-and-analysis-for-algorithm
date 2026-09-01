def hamiltonian_cycle(adj_matrix):
    n = len(adj_matrix)
    path = [-1] * n
    path[0] = 0  # Start at node 0

    def is_valid(v, pos):
        if adj_matrix[path[pos - 1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def backtrack(pos):
        if pos == n:
            # Check if there is an edge back to the starting vertex
            return adj_matrix[path[pos - 1]][path[0]] == 1

        for v in range(1, n):
            if is_valid(v, pos):
                path[pos] = v
                if backtrack(pos + 1):
                    return True
                path[pos] = -1

        return False

    if backtrack(1):
        return path + [path[0]]
    return "No Hamiltonian Cycle exists"

# 5-vertex graph adjacency matrix
matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]
print("Hamiltonian Cycle Path:", hamiltonian_cycle(matrix))
