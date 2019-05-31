import matplotlib.pyplot as plt
import numpy as np
#train.data
#1 2 3 4 5
#0.5 1 4 2 5
x = [2, 4, 8, 11, 16, 20]
y = [3.5, 2.6, 2.5, 2.75, 5.5, 7.0]
fig = plt.figure()
ax = fig.add_subplot(211)
ax.scatter(x=x, y=y, marker='o', c='b')
ax.plot(x, y, label = u'linear', color='blue', linewidth=2)
ax.set_xlabel(u'x axis')
ax.set_ylabel(u'y axis')
plt.legend()
plt.savefig('linear')
#plt.show()
