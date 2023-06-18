import numpy as np

# LUx = b
# trả về L và U
def lu(A):
    # Lấy số hàng
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    # Lặp qua các hàng
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U

# Giải quyết Ly = b
def forward_substitution(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
    return y

# Giải quyết Ux = y
def back_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i+1:], x[i+1:])) / U[i,i]
    return x

# Giải quyết
def lu_solve(A, b):
    L, U = lu(A)
    y = forward_substitution(L, b)
    x = back_substitution(U, y)
    return x

n = int(input("Nhập n = "))
A = np.zeros((n,n))
b = np.zeros(n)

for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'A['+str(i)+']['+ str(j)+']='))
        
for i in range(n):
    b[i] = float(input( 'b[' + str(i) + ']='))
    
print('Kết quả x = ' , lu_solve(A, b))
