import matplotlib.pyplot as plt
import numpy as np
mat=np.loadtxt("blood_sugar.txt")
fig,ax = plt.subplots()

ax.set_xlabel("Age (years)",fontsize=12)
ax.set_ylabel("Blood sugar (gm/dl)",fontsize=12)
s=500
plt.scatter(mat[0:,0], mat[0:,1],s)
fig.savefig('plot.png', format='png',bbox_inches='tight',dpi=300)

