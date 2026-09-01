def set_cover_greedy(universe, subsets):
    universe = set(universe)
    covered = set()
    selected_subsets = []

    while covered != universe:
        best_subset = max(subsets, key=lambda s: len(set(s) - covered))
        selected_subsets.append(best_subset)
        covered.update(best_subset)

    return selected_subsets

U = {1, 2, 3, 4, 5}
S = [[1, 2, 3], [2, 4], [3, 4], [4, 5]]
print("Greedy Set Cover:", set_cover_greedy(U, S))
