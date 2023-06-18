import math
def f(x):
    return math.sin(x)

# Phương pháp dây cung

def secant(x0,x1,e,N):
    print('\n\n*** Phương pháp dây cung ***')
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print('Lỗi khi chia cho 0')
            break
        
        x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
        print('Lần lặp-%d, x2 = %0.10f và f(x2) = %0.10f' % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Không hội tụ')
            break
        
        condition = abs(f(x2)) > e
    print('\n Kết quả: %0.10f' % x2)


# Input
x0 = input('x0 = ')
x1 = input('x1 = ')
e = input('Độ chính xác: ')
N = input('Số bước lớn nhất: ')

# Chuyển sang dạng float
x0 = float(x0)
x1 = float(x1)
e = float(e)

# Chuyển sang dạng số nguyên
N = int(N)

secant(x0,x1,e,N)

