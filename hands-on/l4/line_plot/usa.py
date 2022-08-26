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

def movingaverage (values, window):
    #weights = np.repeat(1.0, window)/window
    weights = np.ones([window,1])/window
    sma = convolve(values, weights, 'valid')
    print(sma.shape)
    return sma


mat0 = genfromtxt("new_cases_usa.dat");
avg=movingaverage(mat0,10)
fig,ax = plt.subplots()
#ax.plot(mat0[:,0], mat0[:,1]/1000, color='C1',marker='o',lw=1.0,markersize=0,mfc='white',markevery=2,label="Daily cases, USA")
ax.plot(avg[:,0], avg[:,1]/1000, color='C0',marker='o',lw=5.0,markersize=0,mfc='white',markevery=2,label="Average")
plt.grid(linestyle=":")
#plt.grid(color='r', linestyle='.', linewidth=0.2)
plt.legend(handlelength=1,loc=0,frameon="True",fontsize=10)
plt.minorticks_off()
ax.tick_params(direction='in')
ax.set_xlabel("Time (days)",fontsize=16,fontweight="bold",fontname="Times New Roman")
ax.set_ylabel("New covid cases (in thousands)",fontsize=16,fontweight="bold",fontname="Times New Roman") 

#ax.set_ylim(ymax= 430,ymin=0)
ax.set_xlim(xmax= 1000,xmin=0)
ax.yaxis.set_major_locator(plt.MultipleLocator(500))
#ax.fill_between([20,35],[-3,-3],[18,18],alpha=0.1,color='C4')
#ax.fill_between([50,80],[0,0],[5000,5000],alpha=0.3,color='C1')
#ax.fill_between([0,50],[0,0],[5000,5000],alpha=0.3,color='C0')
style = dict(size=10, color='black',rotation=90)
ax.text(1, 300, "JAN 2020 ", ha='left', **style)
ax.text(366, 300, "JAN 2021 ", ha='left', **style)
ax.text(731, 300, "JAN 20202 ", ha='left', **style)

plt.tight_layout()
#plt.show()
fig.savefig('new_cases_mv.png', format='png',bbox_inches='tight',dpi=300)
