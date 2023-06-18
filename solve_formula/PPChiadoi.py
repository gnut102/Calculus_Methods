#f(x) = sin(x)
import math
def f(x):
    return math.sin(x)

# pp chia đôi
def bisection(x0,x1,e):
    step = 1
    print('\n\n*** PHƯƠNG PHÁP CHIA ĐÔI ***')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Lần lặp-%d, x2 = %0.10f và f(x2) = %0.10f' % (step, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nKết quả : %0.10f' % x2)

# Input
x0 = input('x0 = ')
x1 = input('x1 = ')
e = input('Độ chính xác: ')

# Chuyển input sang kiểu float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Kiểm tra tính chính xác của các giá trị đoán ban đầu và chia đôi
if f(x0) * f(x1) > 0.0:
    print('Giá trị đầu vào không hợp lệ.')
    print('Thử lại với giá trị khác')
else:
    bisection(x0,x1,e)

