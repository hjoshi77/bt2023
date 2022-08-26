from matplotlib import pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['C', 'Fortran', 'SQL', 'Python']
students = [10,6,15,35]
ax.pie(students, labels = langs,autopct='%1.2f%%')
#plt.show()
plt.tight_layout()
fig.savefig('pie.png', format='png',bbox_inches='tight',dpi=300)
