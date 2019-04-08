import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100, 900, 100)
y = [0.001, 0.005, 0.01, 0.02, 0.022, 0.032, 0.045, 0.049] #own func
y1 = [0.05, 0.065, 0.07, 0.072, 0.08, 0.081, 0.09, 0.15]
#plt.plot(y)
#plt.plot(x)
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y, label = u'Implementation')
ax.plot(x, y1, label = u'SciPy function')
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.show()
