import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter


def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xlabel('Angle ($^{\circ}$)')

# Creating dataset
#np.random.seed(23685752)
#N_points = 10000
n_bins = 180
mat0=np.loadtxt("combine.dat") 
# Creating distribution
# set style for the axes
# Creating histogram
fig, (ax1, ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 4), sharey=True)
ax1.hist(mat0[:,0],bins=n_bins,density=True,color="red",alpha=1.0)
ax2.hist(mat0[:,1],bins=n_bins,density=True,color="blue",alpha=1.0)
ax3.hist(mat0[:,2],bins=n_bins,density=True,color="black",alpha=1.0)
ax1.set_xlabel("Angle ($^{\circ}$)",fontsize=15)
ax2.set_xlabel("Angle ($^{\circ}$)",fontsize=15)
ax3.set_xlabel("Angle ($^{\circ}$)",fontsize=15)
ax1.set_ylabel("Probability density",fontsize=15)

#ax.set_ylim(ymax= 2000,ymin=-50)
ax2.set_xlim(xmax= 180,xmin=0)
labels = ['Inside', 'No gap', 'Outside']
for ax in [ ax1,ax2,ax3]:
    set_axis_style(ax, labels)  
plt.savefig('hst.png', format='png',bbox_inches='tight',dpi=300)
