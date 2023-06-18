import math
# Tìm
def proterm(i, value, x):
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro
 

# Bảng hiệu chia (divided difference table)
def dividedDiffTable(x, y, n):
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    return y
 
# Hàm áp dụng pp nội suy Newton
def applyFormula(value, x, y, n):
    sum = y[0][0]
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i])
    return sum
 
#In bảng hiệu chia
def printDiffTable(y, n):
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 6), "\t",
                               end = " ")
        print("")
 

# Input

n = int(input("Nhập số mốc:"))
N = float(input('Nhập điểm cần nội suy: '))
y = [[0 for i in range(n)] for j in range(n)]
x = []

# Tạo danh sách các điểm mốc x từ 0 đến pi/2
for i in range(n):
    xi = (i * math.pi) / (2 * (n - 1))
    x.append(xi)

# Tính giá trị y tương ứng với các điểm mốc x
for i in range(n):
    y[i][0] = math.sin(x[i])

value = N  # Giá trị x cần nội suy


# Tính bảng hiệu chia
y=dividedDiffTable(x, y, n)

# In bảng hiệu chia
printDiffTable(y, n)
 
# In giá trị nội suy
print("\nGiá trị nội suy tại", value, "là",
        applyFormula(value, x, y, n))
