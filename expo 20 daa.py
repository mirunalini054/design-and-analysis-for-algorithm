def find_min_max(arr, low, high):
    if low == high:
        return arr[low], arr[low]
    
    if high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])

    mid = (low + high) // 2
    min1, max1 = find_min_max(arr, low, mid)
    min2, max2 = find_min_max(arr, mid + 1, high)

    return min(min1, min2), max(max1, max2)

arr = [1000, 11, 445, 1, 330, 3000]
minimum, maximum = find_min_max(arr, 0, len(arr) - 1)
print(f"Min: {minimum}, Max: {maximum}")
