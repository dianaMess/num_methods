import numpy as np
import scipy.linalg as sla
import math
import random
import time
start = time.time()
def chol(A, n):
    L = np.ones((n, n)) * 0
    L[0][0] = math.sqrt(A[0][0])
    for i in range(1, n):
        L[i][0] = A[i][0]/L[0][0]
    for i in range(1, n):
        s = 0
        for k in range(i):
            s = s + L[i][k] * L[i][k]
        temp = A[i][i] - s
        L[i][i] = math.sqrt(temp)
        for j in range(i + 1, n):
            s = 0;
            for k in range(i):
                s = s + L[j][k] * L[i][k]
            temp = A[j][i] - s
            L[j][i] = temp / L[i][i]
    return L

for i in range(500, 600, 100):
    a = np.random.randint(10, size=(i, i))
    for k in range(i):
        for l in range(i):
            if k != l:
                a[k][l] = a[l][k]
    s = np.sum(np.abs(a), axis=1)
    for k in range(i):
        a[k][k] = s[k]
    v = np.random.randint(20, size=i)
    b = a.dot(v)
#    D = chol(a, i)
#    y = sla.solve(D, b)
#    D1 = D.transpose()
#    x = sla.solve(D1, y)
#stop = time.time()
#print(stop - start)
    L = sla.cholesky(a, lower=True)
    t = sla.solve(L, b)
    L1 = L.transpose()
    d = sla.solve(L1, t)
    stop = time.time()
    print(stop - start)
#    if np.allclose(d, x) == True:
#        print('OK')
#    else:
#        print('NO')

