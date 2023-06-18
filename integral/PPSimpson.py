from math import *
import math
# Tính gần dúng tích phân theo công thức simpton
def simpson(n):
    a,b = bounds()
    sum = float()
    oddSum = float()
    evenSum = float()
    h=(b-a)/(2*n) #độ rộng các khoảng

    for i in range(1,n): #đánh giá tất cả các giá trị lẻ của n (không phải đầu tiên và cuối cùng)
        oddSum += f(2*h*i+a)
    for i in range(1,n+1): #đánh giá tất cả các giá trị chẵn của n (không phải đầu tiên và cuối cùng)
        evenSum += f(h*(-1+2*i)+a)

    sum += f(a) + evenSum * 4 + oddSum * 2 + f(b) 
    return sum * h/3

# Nhập 2 cận a, b
def bounds():
    a = 0
    b = 1
    return a,b
# Nhập hàm
def f(x): 
    return((1/((2*math.pi)**(-0.5)))*math.exp(-(x**2)/2))
print(simpson(10))