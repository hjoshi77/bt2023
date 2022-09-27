import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics
  
# Calculating mean and standard deviation
mean = 165
sd = np.linspace(11,20,10)
n=range(0,len(sd))

##z_score=float(input())

x_axis=np.arange(130,200,0.1)
print ("mean", mean ) 
print ("standard deviation",sd )
x=x_axis
j=000
for I in sd:
#for I in sd:
  j=j+1
  fig, ax = plt.subplots()  
  ax.set_xlim(xmax=200,xmin=130)
  ax.set_ylim(ymax=0.04,ymin=0)
  y=norm.pdf(x_axis, mean,I)
  ax.set_xlabel("Height (cm)",fontsize=12)
  ax.set_ylabel("Probability density",fontsize=12)
  plt.grid()
  plt.plot(x,y)
  plt.savefig('norm{}.png'.format(j), format='png',bbox_inches='tight',dpi=300) 
