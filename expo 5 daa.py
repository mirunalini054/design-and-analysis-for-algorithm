def quick_sort(arr, low=0, high=None):
    """Generic in-place Quick Sort algorithm."""
    if high is None:
        high = len(arr) - 1

    def partition(l, h):
        pivot = arr[h]
        i = l - 1
        for j in range(l, h):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

    return arr

numbers = [10, 7, 8, 9, 1, 5]
print("Quick Sorted:", quick_sort(numbers))
