def bin_packing_ffd(items, bin_capacity):
    items.sort(reverse=True)
    bins = []

    for item in items:
        placed = False
        for i in range(len(bins)):
            if sum(bins[i]) + item <= bin_capacity:
                bins[i].append(item)
                placed = True
                break
        if not placed:
            bins.append([item])

    return bins

items = [4, 8, 1, 4, 2, 1, 7, 6]
capacity = 10
packed_bins = bin_packing_ffd(items, capacity)
print(f"Total Bins Used: {len(packed_bins)}, Bins Configuration: {packed_bins}")
