import numpy as np
import matplotlib.pylab as pl
from scipy.optimize import leastsq

data = np.genfromtxt('15cm.dat',delimiter='\t',skip_header=0)

def func(x,p):
    a, b, c, d= p
    return a*np.exp(-(x-b)**2/(2*c**2)) + d

def residuals(p, y, x):
    return y - func(x, p)

x, y = data[:,0], data[:,1]
p0 = [5.09255131e+04,2.49288913e-06,1.25004993e+03,7.22574617e-06] # 初始参数
plsq = leastsq(residuals, p0, args=(y,x))
y2 = func(x,plsq[0])

print (u"拟合参数:", plsq[0]) # 实验数据拟合后的参数

pl.plot(x, y, 'b', label='Experiment data', linewidth=3)
pl.plot(x, y2, 'r--',label='Fitting data', linewidth=2)
pl.xlabel('Time(ps)')
pl.ylabel('Amplitude[a.u.]')
pl.legend()
pl.show()
