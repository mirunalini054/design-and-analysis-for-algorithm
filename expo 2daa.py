import math

def master_theorem(a: float, b: float, k: float, p: float = 0):
    """
    Solves recurrences of form: T(n) = a*T(n/b) + O(n^k * (log n)^p)
    """
    if a < 1 or b <= 1:
        return "Invalid parameters: 'a' must be >= 1 and 'b' must be > 1."
    
    log_b_a = math.log(a, b)
    
    if math.isclose(log_b_a, k, abs_tol=1e-9):
        if p > -1:
            return f"Θ(n^{k} * (log n)^{p + 1})"
        elif p == -1:
            return f"Θ(n^{k} * log(log n))"
        else:
            return f"Θ(n^{k})"
    elif log_b_a > k:
        return f"Θ(n^{log_b_a:.2f})"
    else:
        if p >= 0:
            return f"Θ(n^{k} * (log n)^{p})"
        else:
            return f"Θ(n^{k})"

# Examples
print("Merge Sort T(n) = 2T(n/2) + n:", master_theorem(a=2, b=2, k=1, p=0))
print("Binary Search T(n) = T(n/2) + 1:", master_theorem(a=1, b=2, k=0, p=0))
