import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [6, 4]
plt.rcParams["figure.autolayout"] = True

def f(x):
#   return np.sin(x) + x + x * np.sin(x)
   return np.tan(x) 
def f1(x):
   return np.cos(x) 
def f2(x):
   return np.power(x,10) 
def f3(x):
   return np.exp(-1*np.power((x),2))
plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
#x = np.linspace(-10, 10, 10000)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
plt.xlabel("x")
plt.ylabel("F(x)")
#plt.plot(x*57.32, f2(x), color='C0',label = "x^3")
#plt.plot(x*57.32, f1(x), color='C1',label = "cos x")
plt.plot(x*57.32, f3(x), color='C3',label='$\mathrm{e^{-x^2}}$')
plt.legend()
ax = plt.gca()
ax.set_xlim([-360, 360])
#ax.set_ylim([-1, 1])

plt.savefig('test.png', dpi=100)
