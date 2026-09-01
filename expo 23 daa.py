def assembly_line_scheduling(a, t, e, x):
    """
    a[i][j]: Processing time at station j of line i
    t[i][j]: Transfer time from line i to other line at station j
    e[i]: Entry times, x[i]: Exit times
    """
    num_stations = len(a[0])
    f1 = [0] * num_stations
    f2 = [0] * num_stations

    f1[0] = e[0] + a[0][0]
    f2[0] = e[1] + a[1][0]

    for j in range(1, num_stations):
        f1[j] = min(f1[j - 1] + a[0][j], f2[j - 1] + t[1][j - 1] + a[0][j])
        f2[j] = min(f2[j - 1] + a[1][j], f1[j - 1] + t[0][j - 1] + a[1][j])

    return min(f1[-1] + x[0], f2[-1] + x[1])

a = [[4, 5, 3, 2], [2, 10, 1, 4]]
t = [[0, 7, 4, 5], [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
print("Minimum Time:", assembly_line_scheduling(a, t, e, x))
