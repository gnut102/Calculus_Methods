def seidel(a, x, b):
    n = len(a)
    for j in range(n):
        d = b[j]
        for i in range(n):
            if j != i:
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]
    return x

n = int(input("Nhập n: "))
x = [0] * n
a = []
b = []

for i in range(n):
    row = []
    for j in range(n):
        value = float(input(f"a[{i}][{j}]: "))
        row.append(value)
    a.append(row)
for i in range(n):
    value = float(input(f"b[{i}]: "))
    b.append(value)

print("Giá trị ban đầu của x:", x)

for i in range(10):
    x = seidel(a, x, b)
    print("Lần", i+1, ":", x)
