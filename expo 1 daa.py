def verify_bounds(f, g, c_lower, c_upper, n_start, n_end):
    """
    Checks if f(n) is bounded by c_lower*g(n) <= f(n) <= c_upper*g(n)
    over a range of n values.
    """
    valid = True
    for n in range(n_start, n_end + 1):
        lower_bound = c_lower * g(n)
        upper_bound = c_upper * g(n)
        fn_val = f(n)
        if not (lower_bound <= fn_val <= upper_bound):
            valid = False
            print(f"Failed at n={n}: {lower_bound} <= {fn_val} <= {upper_bound} is False")
    return valid

# Generic Example: f(n) = 3n + 2, g(n) = n
f = lambda n: 3 * n + 2
g = lambda n: n

# Verify 3n <= 3n+2 <= 4n for n >= 2
is_theta = verify_bounds(f, g, c_lower=3, c_upper=4, n_start=2, n_end=100)
print("Fits tight bound Θ(g(n)):", is_theta)
