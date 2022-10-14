from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
from numpy import trapz
from scipy.integrate import simpson
mat=np.loadtxt("test.dat")
x = mat[:,0]
y = mat[:,1]
xs = np.arange(-2.4, 1, 0.01)
#cs = CubicSpline(x, y,bc_type='not-a-knot')
cs = CubicSpline(x, y,bc_type='periodic')
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, cs(xs), label="S")
plt.grid(linestyle=':')
ax.set_ylim(ymin=0)
ax.set_xlim(xmax=1.1,xmin=-2.5)
area = trapz(cs(xs), dx=0.01)
area1 = simpson(cs(xs), dx=0.01)
print("Trapezoidal area =", area)
print("Simpson area =", area1)
plt.fill_between(xs, cs(xs), alpha=0.30,color='green')

plt.savefig('split_fit.png', format='png',bbox_inches='tight',dpi=300)
