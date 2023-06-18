import math
def f(x):
    return((1/((2*math.pi)**(-0.5)))*math.exp(-(x**2)/2))

def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

a = float(input("Nhập cận dưới: "))
b = float(input("Nhập cận trên: "))
n = int(input("Nhập số khoảng: "))

print("Kết quả tích phân theo phương pháp midpoint là: %0.8f" % (midpoint(f, a, b, n)))
