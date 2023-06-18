import numpy as np
import math

# Số điểm mốc n
n = 10

# Tạo mảng x và y để lưu trữ các điểm mốc
x = np.linspace(0, math.pi/2, n)
y = np.sin(x)

xp = float(input('Nhập điểm nội suy: '))

# Đặt giá trị nội suy ban đầu là 0
yp = 0

# Thực hiện nội suy Lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j]) / (x[i] - x[j])

    yp = yp + p * y[i]

# Kết quả
print('Giá trị nội suy tại %.8f là %.8f.' % (xp, yp))
