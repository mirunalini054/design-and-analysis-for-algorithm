def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23
idx = binary_search_recursive(data, 0, len(data) - 1, target)
print("Binary Search Target Index:", idx)
