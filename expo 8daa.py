def solve_tsp(dist_matrix):
    """Generic TSP solver returning minimal distance and full path route."""
    n = len(dist_matrix)
    memo = {}

    def visit(mask, u):
        if mask == (1 << n) - 1:
            return dist_matrix[u][0], [0]
        if (mask, u) in memo:
            return memo[(mask, u)]

        min_cost = float('inf')
        best_path = []

        for v in range(n):
            if not (mask & (1 << v)):
                cost, path = visit(mask | (1 << v), v)
                total_cost = dist_matrix[u][v] + cost
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = [v] + path

        memo[(mask, u)] = (min_cost, best_path)
        return min_cost, best_path

    min_cost, path = visit(1, 0)
    return min_cost, [0] + path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cost, tour = solve_tsp(graph)
print(f"Optimal TSP Cost: {cost}, Path: {tour}")
