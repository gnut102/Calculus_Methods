import math

def max_y(a, n):
    max1 = abs(a[0][0])
    for i in range(1, n):
        for j in range(1):
            if abs(a[i][j]) >= max1:
                max1 = abs(a[i][j])
    return max1

n = int(input("Nhap ma tran cap: "))
c = int(input("Nhap so buoc nhay: "))
esp = float(input("Nhap sai so: "))

count = 0  # so buoc nhay khi thoa man sai so
a = [[0] * 20 for _ in range(20)]
b = [[0] * 1 for _ in range(20)]
x = [[0] * 1 for _ in range(20)]
y = [[0] * 1 for _ in range(20)]
old_lamda = 0.0
lamda, tu, mau = 0.0, 0.0, 0.0

print("Nhap ma tran A:")
for i in range(n):
    a[i] = list(map(float, input().split()))

print("Nhap vector don vi:")
for i in range(n):
    b[i][0] = float(input())

while count <= c:
    tu = 0.0
    mau = 0.0

    for i in range(n):
        for j in range(1):
            y[i][j] = 0.0

    for i in range(n):
        for j in range(1):
            for k in range(n):
                y[i][j] += a[i][k] * b[k][j]

    d = max_y(y, n)

    for i in range(n):
        for j in range(1):
            x[i][j] = y[i][j] / d

    for i in range(n):
        for j in range(1):
            tu += y[i][j] * x[i][j]
            mau += x[i][j] * x[i][j]

    lamda = tu / mau

    for i in range(n):
        for j in range(1):
            b[i][j] = x[i][j]

    for i in range(n):
        for j in range(1):
            print('{:.15f}'.format(x[i][j]), end=' ')
        print()

    print("Gia tri rieng la: ", '{:.15f}'.format(lamda))
    if abs(lamda - old_lamda) < esp:
        break
    else:
        old_lamda = lamda
        count += 1

    print()

print("So buoc nhay: ", count)
