#!/bin/env python
# Using the magic encoding
# -*- coding: utf-8 -*
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt

k=1
m=1
g=9.8
N=m*g
dt=0.01
x=[1]
x2=[1]
v=[0]
v2=[0]
a=[-k*x[0]]
a2=[-k*x2[0]]
t=[0]
mu=0.005
mu2=0.010
for tt in range(10000): 
	t.append(t[-1]+dt)
	a.append(-k*x[-1]-mu*N*np.sign(v[-1]))
	x.append(x[-1]+v[-1]*dt+0.5*a[-1]*dt**2)
	v.append(v[-1]+0.5*(a[-1]+a[-2])*dt)
	a2.append(-k*x2[-1]-mu2*N*np.sign(v2[-1]))
	x2.append(x2[-1]+v2[-1]*dt+0.5*a2[-1]*dt**2)
	v2.append(v2[-1]+0.5*(a2[-1]+a2[-2])*dt)
plt.figure(1)
plt.plot(t,x)
plt.plot(t,x2)
#plt.figure(2)
#plt.axes().set_aspect('equal')
#plt.plot(x,v)
#plt.plot(x2,v2)
plt.show()
