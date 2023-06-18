import numpy as np
import math

# Tính gần đúng đạo hàm bậc hai
def fx(x):
    return(math.sin(x)*math.exp(x)+math.log(x*x*x+1,math.exp(1))) #hàm sin(x).e^x + ln(1+x^3)
n = int(input("Nhập n: "))
x = np.linspace(0, 1, n)
y = np.array([round(fx(x[i]),10) for i in range(len(x))])

h = 1/(n-1)
#sử dụng phương pháp 3 điểm
def midpoint(h, y, i):
    return ((1/(h*h)) * (y[i-1] -2*y[i] + y[i + 1]))
print("----------Đạo Hàm Cấp 2-----------")

for i in range(n):
    if i != 0 and i != n-1:
        print("f''[" , x[i] , "]=" , midpoint(h, y, i))
