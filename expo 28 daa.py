def fractional_knapsack(weights, values, capacity):
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(values))]
    items.sort(key=lambda x: x[0], reverse=True)

    total_value = 0.0
    for ratio, w, v in items:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += ratio * capacity
            break

    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
cap = 50
print("Max Value (Fractional):", fractional_knapsack(weights, values, cap))
