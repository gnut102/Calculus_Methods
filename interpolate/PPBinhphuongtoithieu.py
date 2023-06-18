import numpy as np
import math

def f(x):
    return((1/((2*math.pi)**(-0.5)))*math.exp(-(x**2)/2))
  
def estimated(a, x):
    ans, l = 0, len(a)
    for i in range(l):
        ans = ans * x + a[l-1-i]
    return ans

def BPTTRR(x, y, n):
    sums = [np.sum(np.fromiter((xi**j for xi in x), dtype=float), dtype=float) for j in range(n*2+1)]
    mtr = np.zeros((n+1,n+1))    
    b = np.zeros((n+1,1))
    
    for i in range(n+1):
        for j in range(n+1):
            mtr[i,j] = sums[i+j]
    for j in range(n+1):
        b[j,0] = np.sum(np.fromiter((x[i]**j * y[i] for i in range(len(x))), dtype=float)) 
    # print('Matrix =', mtr)
    # print('b =', b, '\n')
    return np.linalg.solve(mtr, b)
    
x=np.array([i / 40 for i in range(41)])
y=np.array([f(x[i]) for i in range(len(x))])

print('---x---')
print(x)
print('---y---')
print(y, '\n\n')

for deg in range(1, 11):
	print('--- BAC', deg, '---')
	a = BPTTRR(x,y,deg)
	print('+ He so cua da thuc:', np.transpose(a))
	p = estimated(a,x)
	print('+ y_estimated =', p)
	print('+ Bac', deg, ': Sai so:', np.sum(np.fromiter(((y[i]-p[i])**2 for i in range(len(x))), dtype=float)), '\n')
