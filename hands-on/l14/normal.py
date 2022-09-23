import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
fig, ax = plt.subplots()  
  
# Calculating mean and standard deviation
mean = 165
sd = 10
##z_score=float(input())

plt.grid()
x_axis=np.arange(130,200,0.1)
ax.set_xlabel("Height (cm)",fontsize=12)
ax.set_ylabel("Probability density",fontsize=12)
print ("mean", mean ) 
print ("standard deviation",sd )
x=x_axis
y=norm.pdf(x_axis, mean, sd)
plt.plot(x,y)
ax.fill_between(x,y, where = (x-170>1.5*sd) ,alpha=0.3,color='C0')
#ax.fill_between([mean-(sd),mean+(sd)],[norm.pdf(mean-(sd), mean, sd),norm.pdf(mean+(sd), mean, sd)],[0,0],alpha=0.3,color='C0')
ax.set_ylim(ymax=0.04,ymin=0)
ax.set_xlim(xmax=200,xmin=130)
plt.savefig('norm.png', format='png',bbox_inches='tight',dpi=300) 
