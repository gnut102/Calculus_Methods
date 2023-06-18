import math
def f(x):
    return math.sin(x)

# g(x) là đạo hàm của f(x)
def g(x):
    return math.cos(x)

# Phương pháp Newton

def newtonMethod(x0,e,N):
    print('\n\n*** PHƯƠNG PHÁP NEWTON ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Lỗi khi chia cho 0')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Lần lặp-%d, x1 = %0.10f và f(x1) = %0.10f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nKết quả: %0.10f' % x1)
    else:
        print('\nKhông hội tụ.')


# Input
x0 = input('x0 = ')
e = input('Độ chính xác ')
N = input('Số bước lớn nhất: ')

# Chuyển sang dạng float
x0 = float(x0)
e = float(e)

# Chuyển N sang kiểu nguyên
N = int(N)

newtonMethod(x0,e,N)
