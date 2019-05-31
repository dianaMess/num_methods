import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
#linear
x = [2, 4, 8, 11, 16, 20]
y = [3.5, 2.6, 2.5, 2.75, 5.5, 7.0]
fig = plt.figure()
ax = fig.add_subplot(211)
#ax.scatter(x=x, y=y, marker='o', c='b')
#ax.plot(x, y, label = u'linear', color='red', linewidth=2)

#lagrange
x1 = np.array([2, 4, 8, 11, 16, 20])
y1 = np.array([1.57, 3.34, 1.9, 1.91, 8.71, 0])
#fig = plt.figure()
#ax = fig.add_subplot(211)
xnew1 = np.linspace(x1.min(), x1.max(), 300)
line1 = spline(x1, y1, xnew1)
#spline
x2 = np.array([2, 4, 8, 11, 16])
y2 = np.array([3.59, 2.68, 1.43, 2.89, 5.17])
xnew2 = np.linspace(x2.min(), x2.max(), 300)
line2 = spline(x2, y2, xnew2)
#plt.plot(xnew2, line2)


#plot
#ax.scatter(x=x, y=y, marker='o', c='r')
#ax.scatter(x=xnew1, y=line1, marker='o', c='b')
ax.plot(xnew1, line1,label = u'lagrange', color='blue', linewidth=3)
ax.plot(x, y, label = u'linear', color='red', linewidth=3)
ax.plot(xnew2, line2, label = u'spline', color='orange', linewidth=3)
ax.set_xlabel(u'x axis')
ax.set_ylabel(u'y axis')
plt.legend()
plt.savefig('Interpolation')
#plt.show()
