import numpy as np
def phi(i, z, x):
    ans = 1
    n = len(x)
    for j in range(n):
        if i != j:
            ans = ans * (z - x[j]) / (x[i] - x[j])
    return ans

def compute_value(x, y, z):
    s = 0
    n = len(y)
    for i in range(n):
        s = s + y[i] * phi(i, z, x)
    return s

n = int(input())
m = int(input())
x = np.array(n)
y = np.array(n)
z = np.array(m)
f1 = open('example/train.dat', 'r')
f2 = open('example/train.ans', 'r')
f3 = open('example/test.dat', 'r')
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
for i in range(size):
    val = compute_value(x, y, z[i])
    print(val)

