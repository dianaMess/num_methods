import numpy as np
def function(a, b, z):
    return a * z + b

n = int(input())
m = int(input())
x = np.array(n)
y = np.array(n)
z = np.array(m)
f1 = open('example/train.dat', 'r')
f2 = open('example/train.ans', 'r')
f3 = open('example/test.dat', 'r')
i = 1;
for elem in f1:
    x = list(map(float,elem.split()))
for elem in f2:
    y = list(map(float,elem.split()))
for elem in f3:
    z = list(map(float,elem.split()))
f1.close()
f2.close()
f3.close()

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
    
