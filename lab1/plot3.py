import matplotlib.pyplot as plt
import numpy as np
x = np.arange(100, 600, 100)
#print(x)
y = [0.05, 0.627, 0.09, 0.15, 0.27] #scipy func
y1 = [0.85, 3.35, 11, 23.5, 45.5] 
fig = plt.figure()
ax = fig.add_subplot(211)
ax.plot(x, y1, label = u'Implementation', linewidth=3)
ax.plot(x, y, label = u'SciPy function', linewidth=3, color='red')
#ax.plot(x, y1)
#ax.plot(x, y)
ax.set_xlabel(u'Matrix size')
ax.set_ylabel(u'Time')
plt.legend()
plt.savefig('pic_chol')
#plt.show()
