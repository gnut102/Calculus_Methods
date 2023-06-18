def f(t,y):

    return 2*y*t

n = int(input('Nhập n = '))
a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
ya = float(input('Nhập y(a) = '))

#h = (b-a)/n
h = 0.1
w = ya
t = a

for i in range(n):
    k1 = h * f(t, w)
    k2 = h * f((t + h/2), (w + k1/2))
    k3 = h * f((t + h/2), (w + k2/2))
    k4 = h * f((t + h), (w + k3))
    w = w + (k1 + 2*k2 + 2*k3 + k4)/6
    t = a + (i+1)*h
    print ("i =", i+1, ": t = ", t, "   w =", w)

print("y(", b, ") = ", w)
