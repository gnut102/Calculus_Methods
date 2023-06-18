from pprint import pprint
from numpy import array, zeros, diag, diagflat, dot

def jacobi(A, b, N, x=None):
    if x is None:
        x = zeros(len(A[0]))

    D = diag(A) #lấy các phần từ trên đường chéo chính
    R = A - diagflat(D)  #(I-A)

    for _ in range(N):  #tìm nghiệm của phương trình
        x = (b - dot(R, x)) / D
    return x

n = int(input("Nhập n: "))
A = []
b = []

for i in range(n):
    row = []
    for j in range(n):
        value = float(input(f"A[{i}][{j}]: "))
        row.append(value)
    A.append(row)
for i in range(n):
    value = float(input(f"b[{i}]: "))
    b.append(value)

guess = array([0] * n)

sol = jacobi(array(A), array(b), N=50, x=guess)

print("A:")
pprint(A)

print("b:")
pprint(b)

print("x:")
pprint(sol)
