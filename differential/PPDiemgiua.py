import numpy as np

def g(t, y):
    return 2*t*y

n = int(input('Nhập n = '))
a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
ya = float(input('Nhập y(a) = '))

h = (b-a)/n
t = a
w = ya

for i in range(n):
    w = w + h * g(t + h/2, w + h/2 * g(t, w))
    t = a + (i+1) * h
    print ("i =", i+1, ": t = ", t, "   w =", w)
print("y(", b, ") = ", w)

