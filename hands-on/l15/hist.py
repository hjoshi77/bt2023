import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
 
# Creating dataset
#np.random.seed(23685752)
#N_points = 10000
n_bins = 5
mat0=np.loadtxt("plant.dat") 
# Creating distribution
 
# Creating histogram
fig, ax = plt.subplots()
#ax.hist(mat0[:,1])
ax.hist(mat0[:,1],bins=n_bins,density=True,alpha=0.3)
ax.hist(mat0[:,0],bins=n_bins,density=True,alpha=0.3)
#ax.set_xlabel("Height (cm)",fontsize=12))
ax.set_ylabel("Probability density",fontsize=12)

#ax.set_ylim(ymax= 2000,ymin=-50)
#ax.set_xlim(xmax= 180,xmin=0)
plt.savefig('hst.png', format='png',bbox_inches='tight',dpi=300)
