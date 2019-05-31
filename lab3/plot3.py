from scipy.interpolate import spline
import numpy as np
import matplotlib.pyplot as plt
x = np.array([2, 4, 8, 11, 16])
y = np.array([3.59, 2.68, 1.43, 2.89, 5.17])
xnew = np.linspace(x.min(), x.max(), 300)
line = spline(x, y, xnew)
plt.plot(xnew, line)
plt.show()
