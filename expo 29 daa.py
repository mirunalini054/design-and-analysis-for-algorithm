def subset_sum(arr, target):
    solutions = []

    def backtrack(index, current_subset, current_sum):
        if current_sum == target:
            solutions.append(current_subset[:])
            return
        if current_sum > target or index >= len(arr):
            return

        # Include arr[index]
        current_subset.append(arr[index])
        backtrack(index + 1, current_subset, current_sum + arr[index])
        current_subset.pop()

        # Exclude arr[index]
        backtrack(index + 1, current_subset, current_sum)

    backtrack(0, [], 0)
    return solutions

data = [10, 7, 5, 18, 12, 20, 15]
target_sum = 35
print("Subsets summing to target:", subset_sum(data, target_sum))
