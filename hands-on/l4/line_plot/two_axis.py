import matplotlib as mpl
import math
from matplotlib.ticker import AutoMinorLocator
from matplotlib import pyplot as plt
import numpy as np
import scipy.optimize as opt
from glob import glob
from pylab import genfromtxt 
from scipy.signal import convolve

mpl.rcParams["axes.labelsize"]=12
mpl.rcParams["xtick.labelsize"]=12
mpl.rcParams["ytick.labelsize"]=12
mpl.rcParams["legend.fontsize"]=12
mpl.rcParams['lines.linewidth'] = 2


mat0 = genfromtxt("new_cases.dat");
mat1 = genfromtxt("new_cases_usa.dat");

fig,ax = plt.subplots()
ax2 = ax.twinx()

ax.plot(mat0[:,0], mat0[:,1]/1000, color='C0',marker='o',lw=1.0,markersize=0,mfc='white',markevery=2,label="Daily cases, India")
ax2.plot(mat0[:,0], mat0[:,2]/1000, color='C1',marker='o',lw=1.0,markersize=0,mfc='white',markevery=2,label="Cumulative cases")

plt.grid(linestyle=":")

ax.legend(handlelength=1,loc=2,frameon="True",fontsize=10)
ax2.legend(handlelength=1,loc=6,frameon="True",fontsize=10)

plt.minorticks_off()

ax.tick_params(direction='in')

ax.set_xlabel("Time (days)",fontsize=16,fontweight="bold",fontname="Times New Roman")
ax.set_ylabel("New covid cases (in thousands)",fontsize=16,fontweight="bold",fontname="Times New Roman") 
ax2.set_ylabel("Cumulative cases (in thousands)",fontsize=16,fontweight="bold",fontname="Times New Roman") 

ax.set_ylim(ymax= 430,ymin=0)
ax.set_xlim(xmax= 1000,xmin=0)
ax.yaxis.set_major_locator(plt.MultipleLocator(100))

style = dict(size=10, color='black',rotation=90)
ax.text(1, 300, "JAN 2020 ", ha='left', **style)
ax.text(366, 300, "JAN 2021 ", ha='left', **style)
ax.text(731, 300, "JAN 20202 ", ha='left', **style)


plt.tight_layout()
#plt.show()
fig.savefig('new_cases.png', format='png',bbox_inches='tight',dpi=300)
