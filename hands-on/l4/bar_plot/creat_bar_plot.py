import numpy as np
import matplotlib.pyplot as plt
from pylab import genfromtxt
 
  
# creating the dataset
#data = np.loadtxt('medals.txt',dtype=str) 
data = genfromtxt ("medals.txt")

# set width of bar
barWidth = 0.20

fig = plt.subplots(figsize =(12, 8)) 
fig,ax = plt.subplots()

# Set position of bar on X axis
br1 = np.arange(len(data[:,0]))
br2 = [x + barWidth for x in br1]
br3 = [x + barWidth for x in br2]
 
# Make the plot
plt.bar(br1, data [:,0], color ="C0", width = barWidth,
        edgecolor ='grey', label ='Gold')
plt.bar(br2, data[:,1], color ="C1", width = barWidth,
        edgecolor ='grey', label ='Silver')
plt.bar(br3, data[:,2], color ="C3", width = barWidth,
        edgecolor ='grey', label ="Bronze")  
plt.xlabel('Country', fontweight ='bold', fontsize = 15)
plt.ylabel('No of Medals', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(data[:,0]))],
        ['Aus', 'Eng', 'Can', 'Ind', 'NZ'])
plt.grid(linestyle=":") 
#ax.set_ylim(ymax= 100,ymin=0) 
plt.legend()
##plt.tight_layout()
plt.savefig('bar.png', format='png',bbox_inches='tight',dpi=300)

