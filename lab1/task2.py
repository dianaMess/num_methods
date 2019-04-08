import numpy as np
import scipy.linalg as sl
import time
#start = time.time()
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

for i in range(2, 5, 1):
#    a = np.random.randint(2, size=(i, i))
#    np.fill_diagonal(a, 100)
    a = np.random.rand(i, i)
    s = np.sum(np.abs(a), axis=1)
    for j in range(i):
        a[j][j] += s[j]
 
    v = np.random.randint(10, size=i)
    y = a.dot(v)

    B = np.diag(a)
    C = np.diag(a, 1)
    A = np.diag(a, -1)
    A1 = [0] * 1
    C1 = [0] * 1
    C = C.tolist()
    C2 = C.copy()
    A1.extend(A)
    C.extend(C1)
    B = B.tolist()
    d = sweep(A1, B, C, y, i)
#stop = time.time()
#print(stop - start)    
    #метод прогонки в numpy
    A2 = [0] * 1
    A = A.tolist()
    A.extend(A2)
    C1.extend(C2)
    D = [C1, B, A]
    w = sl.solve_banded((1, 1), D, y)
#stop = time.time()
#print(stop - start)    
 
    if np.allclose(w, d) == True:
        print('OK')



