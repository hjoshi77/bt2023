from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

import math


l=np.loadtxt("height.dat")

mean_men=l[:,0]
st_men= l[:,1]
mean_wm=l[:,2]
st_wm= l[:,3]

N=5
ind = np.arange(N)  # the x locations for the groups
width = 0.3    

for i in range(5):
    # Stringddo determine the type and density of the hatch.
    # For example, '///' is denser than '/'.
    hatch_str = "/"*2
fig, ax = plt.subplots()

rects1 = ax.bar(ind, mean_men, width, color='C0', yerr=st_men, edgecolor = ["k"]*len(ind),capsize=3)
rects2 = ax.bar(ind + width, mean_wm, width, color='C1', yerr=st_wm, edgecolor = ["k"]*len(ind),capsize=3)
# for making hatch in structure
for bar in rects2:
 bar.set_hatch(hatch_str)
   
# done
ax.set_ylabel('Average height (cm)',fontsize=16)
ax.set_xticks(ind + width /2 )
plt.xticks(rotation=0)
ax.set_xticklabels(('India','USA','China','England','Netherlands'),fontsize=16)
ax.legend((rects1[0], rects2[0]), ('Men', 'Women'),loc=0)
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
ax.set_ylim(ymax=187,ymin=150)
plt.grid(linestyle=":")
plt.xticks(rotation = 45)
autolabel(rects1)
autolabel(rects2)
plt.tight_layout()
fig.savefig('height.png', format='png', dpi=1600)
