import numpy as np
def sweep(a, b, c, f, n):
    alpha = [0] * (n + 1)
    beta = [0] * (n + 1)
    a[0] = 0
    c[n - 1] = 0
    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i]/d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x = [0] * n
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x


def generateSpline(x, y):
    x = np.asarray(x)
    n = x.shape[0] - 1
    h = (x[n] - x[0]) / n
    a = np.array([0] + [1] * (n - 1) + [0]) 
    b = np.array([1] + [4] * (n - 1) + [1]) 
    c = np.array([0] + [1] * (n - 1) + [0]) 
    f = np.zeros(n + 1)
    for i in range(1, n):
        f[i] = 3 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2
    s = sweep(a, b, c, f, n + 1)
    A = np.zeros(n)
    B = np.zeros(n)
    C = np.zeros(n)
    D = np.zeros(n)
    B = s.copy()
    for i in range(n):
#        B[i] = s[i]
        A[i] = (B[i + 1] - B[i]) / (3 * h)
        C[i] = (y[i + 1] - y[i]) / h - (B[i + 1] + 2 * B[i]) * h / 3
        D[i] = y[i]
    return A, B, C, D

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

A, B, C, D = generateSpline(x, y)
n = len(x)
for i in range(1, n - 1):
#    while z[i - 1] >= x[i - 1] and z[i - 1] < x[i]:
    value = A[i - 1] * (z[i - 1] - x[i - 1]) ** 3 + B[i - 1] * (z[i - 1] - x[i - 1]) ** 2 + C[i - 1] * (z[i - 1] - x[i - 1]) + D[i - 1]
    print(value)

