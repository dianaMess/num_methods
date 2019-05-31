import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100, 700, 100)
y = [1.47, 11, 29, 71 ,136, 223]
y1 = [0.04, 0.081, 0.098, 0.13, 0.28, 0.33]
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y, label = u'Implementation', linewidth=5)
ax.plot(x, y1, label = u'SciPy function', color='red', linewidth=5)
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.savefig('pic_gauss')
#plt.plot(y)
#plt.plot(x)
#plt.show()
