def gauss_elimination(A, b):
    n = len(b)
    
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
    
    return x

# Example usage
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

result = gauss_elimination(A, b)
print(result)