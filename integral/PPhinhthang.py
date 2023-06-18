import math
def f(x):
    return((1/((2*math.pi)**(-0.5)))*math.exp(-(x**2)/2))

# Phương pháp hình thang tính xấp xỉ tích phân
def trapezoidal(x0,xn,n):
    # độ rộng
    h = (xn - x0) / n
    
    j = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        j = j + 2 * f(k)
    
    return j * h/2
    
# Input
a = float(input("Nhập cận dưới: "))
b = float(input("Nhập cận trên: "))
n = int(input("Nhập số khoảng: "))

print("Kết quả tích phân theo phương pháp hình thang là: %0.8f" % (trapezoidal(a, b, n)))

