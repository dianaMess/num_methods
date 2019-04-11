import matplotlib.pyplot as plt
import numpy as np
x = np.arange(30, 55, 5)
#implementation
#y = [21, 139]
y = [0.04, 0.053, 0.063, 0.072, 0.086]
y1 = [1.24, 1.41, 2.12, 2.5, 3.7]
#scipy
#y1 = []
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y, label = u'Seidel', color='blue', linewidth=5)
ax.plot(x, y1, label = u'Jacobi', color='red', linewidth=5)
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.savefig('pic_show')
#plt.plot(y)
#plt.plot(x)
#plt.show()
