import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
fig, ax = plt.subplots()  
x_axis = np.arange(-100, 100, 1)
  
# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
ax.set_xlabel("Distribution",fontsize=12)
ax.set_ylabel("Probability density",fontsize=12)
print ("mean", mean ) 
print ("standard deviation",sd ) 
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
ax.fill_between([mean-sd,mean+sd],[0,0],[1,1],alpha=0.3,color='C0')
#ax.fill_between([mean-2*sd,mean+2*sd],[0,0],[1,1],alpha=0.3,color='C1')
ax.set_ylim(ymax= 0.008,ymin=0)
ax.set_xlim(xmax= 100,xmin=-100)
plt.savefig('norm.png', format='png',bbox_inches='tight',dpi=300) 
