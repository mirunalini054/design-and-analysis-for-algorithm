def knapsack_01(weights, values, capacity):
    """Solves 0/1 Knapsack and returns max value with selected item indices."""
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Reconstruction of chosen items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
cap = 5
max_val, items = knapsack_01(weights, values, cap)
print(f"Max Value: {max_val}, Selected Item Indices: {items}")
