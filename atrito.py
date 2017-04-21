#!/bin/env python
# Using the magic encoding
# -*- coding: utf-8 -*
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

k=1
m=1
g=9.8
dt=0.01
x=[1]
v=[0]
a=[-k*x[0]]
t=[0]
mu=0.003
N=m*g
for tt in range(10000): 
	t.append(t[-1]+dt)
	x.append(x[-1]+v[-1]*dt+0.5*a[-1]*dt**2)
	a.append(-k*x[-1]-mu*N*np.sign(v[-1]))
	v.append(v[-1]+0.5*(a[-1]+a[-2])*dt)
plt.figure(1)
plt.plot(t,x)
#plt.axes().set_aspect('equal')
plt.show()
