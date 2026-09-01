import numpy as np

def strassen_general(A, B):
    """Generic Strassen algorithm handling non-power-of-2 matrices via padding."""
    A = np.array(A)
    B = np.array(B)
    
    n, m = A.shape
    p = B.shape[1]
    
    # Pad matrices to nearest power of 2
    max_dim = max(n, m, p)
    next_pow2 = 1 << (max_dim - 1).bit_length()
    
    A_padded = np.pad(A, ((0, next_pow2 - n), (0, next_pow2 - m)))
    B_padded = np.pad(B, ((0, next_pow2 - m), (0, next_pow2 - p)))

    def _strassen(X, Y):
        sz = len(X)
        if sz == 1:
            return X * Y
        
        mid = sz // 2
        A11, A12, A21, A22 = X[:mid, :mid], X[:mid, mid:], X[mid:, :mid], X[mid:, mid:]
        B11, B12, B21, B22 = Y[:mid, :mid], Y[:mid, mid:], Y[mid:, :mid], Y[mid:, mid:]
        
        M1 = _strassen(A11 + A22, B11 + B22)
        M2 = _strassen(A21 + A22, B11)
        M3 = _strassen(A11, B12 - B22)
        M4 = _strassen(A22, B21 - B11)
        M5 = _strassen(A11 + A12, B22)
        M6 = _strassen(A21 - A11, B11 + B12)
        M7 = _strassen(A12 - A22, B21 + B22)
        
        C = np.zeros((sz, sz), dtype=X.dtype)
        C[:mid, :mid] = M1 + M4 - M5 + M7
        C[:mid, mid:] = M3 + M5
        C[mid:, :mid] = M2 + M4
        C[mid:, mid:] = M1 - M2 + M3 + M6
        return C

    C_padded = _strassen(A_padded, B_padded)
    return C_padded[:n, :p]

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
print("Matrix Product:\n", strassen_general(A, B))
