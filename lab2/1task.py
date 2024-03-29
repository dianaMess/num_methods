import numpy as np
from scipy.spatial import distance
import scipy.linalg as sla
import time
start = time.time()
def seidel(A, f, x, n):
    xnew = np.zeros(n)
    for i in range(n):
        s = 0
        for j in range(i):
            s = s + A[i][j] * xnew[j]
        for j in range(i + 1, n):
            s = s + A[i][j] * x[j]
        xnew[i] = (f[i] - s) / A[i][i]
    return xnew

def norm(x, xnew, eps, n):
    if distance.euclidean(x, xnew) > eps:
        return False
    return True

def solve(A, f, eps, n):
    xnew = np.zeros(n)
    while True:
        x = xnew.copy()
        xnew = seidel(A, f, x, n)
        if norm(x, xnew, eps, n):
            break
    return x

#n = int(input())
#a = [[]] * n
#for i in range(n):
#	r = list(map(int,input().split()))
#	a[i] = r
#f = list(map(int,input().split()))
#eps = int(input())
eps = 0.001
#y = sla.solve(a, f)
#x = solve(a, f, eps, n)
#print(y)
#print(x)
for i in range(50, 55, 5):
#    c = np.random.randint(5, size=(i, i))
#    np.fill_diagonal(c, 30)
    c = np.random.randint(5, size=(i, i))
    s = np.sum(np.abs(c), axis=1)
    for j in range(i):
        c[j][j] += s[j]
    v = np.random.randint(5, size=i)
    y = c.dot(v)
    d = np.zeros((i, i))
    d[:] = c
    w = sla.solve(d, y)
    x = solve(d, y, eps, i)
#    print(w)
#    print(x)
    stop = time.time()
    print(stop - start)
    if np.allclose(x, w) == True:
        print("OK")
    else:
        print("NO")
