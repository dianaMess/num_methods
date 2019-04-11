import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100, 600, 100)
#implementation
y = [0.31, 1.31, 2.62, 4.8, 7.67]
#scipy
y1 = [0.006, 0.059, 0.071, 0.21, 0.32]
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y, label = u'Implementation', color='blue', linewidth=5)
ax.plot(x, y1, label = u'SciPy function', color='red', linewidth=5)
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.savefig('pic_seidel')
#plt.plot(y)
#plt.plot(x)
#plt.show()
