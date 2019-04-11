import numpy
import numpy as np
import scipy.linalg as sla
import time
#start = time.time()
def run(A, f, n):
   for i in range(n):
       for j in range(i + 1, n):
           tmp = A[j][i] / A[i][i]
           for k in range(i + 1, n):
               A[j][k] = A[j][k] - tmp * A[i][k]
           f[j] -= tmp * f[i]
           A[j][i] = 0
   for i in range(n - 1, -1, -1):
       f[i] = f[i] / A[i][i]
       A[i][i] = 1
       for j in range(i - 1, -1, -1):
           f[j] = f[j] - f[i] * A[j][i]
           A[j][i] = 0
   return f


for i in range(100, 200, 100):
#    c = np.random.randint(5, size=(i, i))
#    np.fill_diagonal(c, 200)
    v = np.random.randint(20, size=i)
    c = np.random.rand(i, i)
    s = np.sum(np.abs(c), axis=1)
    for j in range(i):
        c[j][j] += s[j]
    y = c.dot(v)
    x = sla.solve(c, y)
    s = run(c, y, i)
#stop = time.time()
#print(stop - start)
    if np.allclose(x, s) == True:
        print('OK')
    else:
        print('NO')
#    if np.allclose(x, w) == True:
#    if np.allclose(x, w) == True:
