def gauss_seidel(A, b, x0, tol=1e-6, max_iter=100):
    n = len(A)
    x = x0.copy()
    
    for _ in range(max_iter):
        x_new = x.copy()
        
        for i in range(n):
            sigma = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]
        
        if all(abs(x[i] - x_new[i]) < tol for i in range(n)):
            break
    
    return x

# Example system of linear equations:
A = [[0.43, 1.24, -0.58],
     [0.74, 0.83, 1.17],
     [1.43, -1.58, 0.83]]
b = [2.71, 1.26, 1.03]
x0 = [0, 0, 0]

# Solve the system using Gauss-Seidel method
solution = gauss_seidel(A, b, x0)

print("Solution:", solution)