import time
import sys

def profile_function(func, *args):
    """Generic profiler to measure execution time of any function."""
    start_time = time.perf_counter()
    result = func(*args)
    elapsed_time = time.perf_counter() - start_time
    return result, f"{elapsed_time:.6f} seconds"

# Iterative Factorial (O(n) time, O(1) space)
def factorial_iterative(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

# Recursive Factorial (O(n) time, O(n) space)
def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n - 1)

sys.setrecursionlimit(2000)
num = 500
_, t_iter = profile_function(factorial_iterative, num)
_, t_rec = profile_function(factorial_recursive, num)

print(f"Iterative Execution Time: {t_iter}")
print(f"Recursive Execution Time: {t_rec}")
