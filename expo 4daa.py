def merge_sort(arr, key=lambda x: x, reverse=False):
    """Generic Merge Sort supporting custom key functions and ordering."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key=key, reverse=reverse)
    right = merge_sort(arr[mid:], key=key, reverse=reverse)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        left_val, right_val = key(left[i]), key(right[j])
        condition = (left_val > right_val) if reverse else (left_val <= right_val)
        
        if condition:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

data = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(data))
