import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
 
# Creating dataset
#np.random.seed(23685752)
#N_points = 10000
n_bins = 180
# Creating distribution
mat0=np.loadtxt("inside_hst.dat") 
mean=np.mean(mat0[:,1]) 
std=np.std(mat0[:,1]) 
mod = stats.mode(mat0[:,1])
med=np.median(mat0[:,1]) 
print("mean=",mean)
print("mode=",mod[0])
print("median=",med)
print("standard deviation=",std)
# Creating histogram
fig, ax = plt.subplots()
#ax.hist(mat0[:,1])
ax.hist(mat0[:,1],bins=n_bins,density=True)
ax.set_ylabel("Probability density",fontsize=12)

#ax.set_ylim(ymax= 2000,ymin=-50)
ax.set_xlim(xmax= 180,xmin=0)
plt.savefig('hst.png', format='png',bbox_inches='tight',dpi=300)
