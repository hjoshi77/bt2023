import matplotlib.pyplot as plt
import numpy as np
import scipy 
from scipy import stats
mat=np.loadtxt("wing_length.dat")
fig,ax = plt.subplots()
ax.set_xlabel("Age (days)",fontsize=12)
ax.set_ylabel("Wing length (cm)",fontsize=12)
s=50
coef=np.polyfit(mat[0:,0],mat[0:,1], 1) 
slope, intercept, r, p, stderr=scipy.stats.linregress(mat[0:,0],mat[0:,1])
print (coef)
#print (fit)
poly1d_fn = np.poly1d(coef)
plt.scatter(mat[0:,0], mat[0:,1],s)
plt.plot(mat[0:,0],poly1d_fn(mat[0:,0]),color='C1',linestyle='--')
plt.fill_between(mat[0:,0], poly1d_fn(mat[0:,0])+(10*stderr), poly1d_fn(mat[0:,0])-(10*stderr), alpha=0.30)
fig.savefig('plot.png', format='png',bbox_inches='tight',dpi=300)

