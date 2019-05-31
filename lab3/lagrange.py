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
for i in range(size):
    val = compute_value(x, y, z[i])
    print(val)

