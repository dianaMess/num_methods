import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100, 600, 100)
#implementation
y = [21, 139]
#scipy
y1 = []
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y, label = u'Implementation', color='blue', linewidth=5)
ax.plot(x, y1, label = u'SciPy function', color='red', linewidth=5)
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.savefig('pic_jacobi')
#plt.plot(y)
#plt.plot(x)
#plt.show()
