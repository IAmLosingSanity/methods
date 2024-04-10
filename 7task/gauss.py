def gauss_elimination(A, b):
    n = len(b)
    if len(A) != n or len(A[0]) != n:
        raise ValueError("Matrix A must be a square matrix")
    if len(b) != n:
        raise ValueError("Vector b must have the same length as A")
    
    # Forward Elimination
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    
    # Back Substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i+1, n):
            x[i] -= A[i][j] / A[i][i] * x[j]
    
    # Check the solution
    residual = [b_i - sum(x_i * A_i_j for x_i, A_i_j in zip(x, A_i)) for A_i, b_i in zip(A, b)]
    solution_ok = all(abs(r) < 1e-10 for r in residual)
    return x, solution_ok

# Example usage
A = [[6, 1, -1, 2],
     [2, 14, -4, 5],
     [4, 7, 16, 3],
     [-7, 6, 3, 19]]
b = [25, 90, -38, 33]

result, ok = gauss_elimination(A, b)
print(result)
print(f"Solution ok: {ok}")

