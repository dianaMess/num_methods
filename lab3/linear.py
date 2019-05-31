import numpy as np
def function(a, b, z):
    return a * z + b

n = int(input())
m = int(input())
x = np.array(n)
y = np.array(n)
z = np.array(m)
f = open('f.txt', 'r')
i = 1;
for elem in f:
    if i == 1:
        x = list(map(float,elem.split()))
    elif i == 2:
        y = list(map(float,elem.split()))
    else:
        z = list(map(float,elem.split()))
    i += 1
f.close()

size = len(z)
v = np.zeros(size)
k = 0
l = 0
for i in range(1, n):
    a = (y[i] - y[i - 1])/(x[i] - x[i - 1])
    b = (y[i - 1] - a * x[i - 1])
    while (k < size) and (z[k] >= x[i - 1]) and (z[k] <= x[i]):
        v[l] = function(a, b, z[k])
        l += 1
        k += 1
size = len(v)
for i in range(size):
    print(v[i], end = ' ')     
    
