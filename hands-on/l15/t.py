import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

rv = t(df=1, loc=0, scale=1)
x = np.linspace(-5, 5, 100)
#x = np.linspace(rv.ppf(0.0001), rv.ppf(0.9999), 100)
y = rv.pdf(x) 

plt.xlim(-5,5)
plt.plot(x,y)
plt.savefig('t_dist.png', format='png',bbox_inches='tight',dpi=300) 
