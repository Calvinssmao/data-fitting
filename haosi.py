import numpy as np
import matplotlib.pyplot as plt 

def func(x,p):
    a, b, c, d= p
    return a*np.exp(-(x-b)**2/(2*c**2)) + d 

p0 = [1,0,1,0]
x = np.linspace(2*np.pi, (-2)*np.pi, 100)
y = func(x, p0)

plt.plot(x, y)
plt.show()