import math

n = int(input("Nhap ma tran cap: "))
c = int(input("Nhap so lan hoi tu: "))

truc_giao_i = 0
di = 0
x0 = [[0] * 1 for _ in range(20)]
y = [[0] * 1 for _ in range(20)]
a = [[0] * 20 for _ in range(20)]
b = [[0] * 1 for _ in range(20)]
lamda = 0

print("Nhap ma tran A:")
for i in range(n):
    a[i] = list(map(float, input().split()))

print("Nhap vector don vi:")
for i in range(n):
    b[i][0] = float(input())

while c > 0:
    for i in range(n):
        for j in range(1):
            y[i][j] = 0

    for i in range(n):
        for j in range(1):
            for k in range(n):
                y[i][j] += a[i][k] * b[k][j]

    truc_giao_i = 0
    for i in range(n):
        for j in range(1):
            truc_giao_i += pow(y[i][j], 2)

    di = math.sqrt(truc_giao_i)

    for i in range(n):
        for j in range(1):
            x0[i][j] = y[i][j] / di

    lamda = 0
    for i in range(n):
        for j in range(1):
            lamda += y[i][j] * x0[i][j]

    for i in range(n):
        for j in range(1):
            b[i][j] = x0[i][j]

    for i in range(n):
        for j in range(1):
            print('{:.15f}'.format(x0[i][j]), end=' ')
        print()

    print("Gia tri rieng lamda la: ", '{:.15f}'.format(lamda))
    print()

    c -= 1
