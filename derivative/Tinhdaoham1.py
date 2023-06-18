import numpy as np
import math

# Tính gần đúng đạo hàm bậc nhất theo Three-Point Endpoint và Three-Point Midpoint
#n = int(input('Nhập n = '))
def fx(x):
    return(math.sin(x)*math.exp(x)+math.log(x*x*x+1,math.exp(1))) #hàm sin(x).e^x + ln(1+x^3)
n = int(input("Nhập n:"))
#n = 50
x = np.linspace(0, 1, n)
y = np.array([fx(x[i]) for i in range(len(x))])

# for i in range(n):
#     x[i] = float(input( 'x['+str(i)+']='))
#     #y[i] = float(input( 'y['+str(i)+']='))
#     y[i] = fx(x[i])

t = 1
h = x[1] - x[0]
#Sử dụng phương pháp 3 điểm
def endpoint(h, y, i, t):
    return ((1/(2*h)) * (-3*y[i] + 4*y[i + t] - y[i + 2*t]))
def midpoint(h, y, i):
    return (1/(2*h)) * (y[i+1]-y[i-1])

# for i in range(n):
#     print (i,"f(",x[i],")=  ", y[i] )

print("--------------Đạo hàm bậc nhất--------------")
for i in range(n):
    if i == 0:
        print(i,"f'[", x[i] , "]=" , endpoint(h, y, i, t))
    elif i == n-1:
        print(i,"f'[" , x[i] , "]=" , endpoint(-h, y, i, -t))
    else:
        print(i,"f'[" , x[i] , "]=" , midpoint(h, y, i))
