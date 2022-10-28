import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
from scipy.integrate import simpson

# Calculating mean and standard deviation
mean = 3
sd = 3 
mean1=2
sd1=2
##z_score=float(input())

fig, ax = plt.subplots(2, 1, figsize=(10,7)) 
x=np.arange(-10,10.1,0.1)
x_int=np.arange(0,100.1,0.01)
y0=norm.pdf(x, mean,sd)
y1=norm.pdf(x, mean1,sd1)
y0_i=norm.pdf(x_int,mean,sd)
y1_i=norm.pdf(x_int,mean1,sd1)

area0=simpson(y0_i,dx=0.01) 
print(area0)
ax[0].plot(x,y0)
ax[1].plot(x,y1)
ax[0].set_xlim(xmax=10,xmin=-10)
ax[1].set_xlim(xmax=10,xmin=-10)
ax[0].set_ylim(ymax=0.20,ymin=0)
ax[1].set_ylim(ymax=0.20,ymin=0)
ax[0].xaxis.set_major_locator(plt.MultipleLocator(3))
ax[1].xaxis.set_major_locator(plt.MultipleLocator(3))
ax[1].yaxis.set_major_locator(plt.MultipleLocator(0.05))
ax[0].yaxis.set_major_locator(plt.MultipleLocator(0.05))
#ax.yaxis.set_minor_locator(plt.MultipleLocator(250))

ax[1].set_xlabel("X",fontsize=12)
ax[1].set_ylabel("Y",fontsize=12)
ax[0].set_ylabel("Y",fontsize=12)
ax[0].grid(linestyle = '--')
ax[1].grid(linestyle = '--')
ax[0].fill_between(x_int, y0_i, alpha=0.30,color='green')
ax[1].fill_between(x_int, y1_i, alpha=0.30,color='red')
ax[0].annotate('Area = 0.841', xy=(-9, 0.15), xytext=(2, 0.08))
ax[1].annotate('Area = 0.841', xy=(-9, 0.15),xytext=(1, 0.15))
plt.savefig('answer4.png', format='png',bbox_inches='tight',dpi=300) 
