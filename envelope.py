import numpy as np 
from math import pi, sqrt, sin, cos, atan2, acos
from Config import Config
w = Config.VI/Config.VD

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Q(s):
	return sqrt(1 + w**2 -2*w*sin(s))

def get_phi(s):
	cphi = w*cos(s)/Q(s)
	sphi = (1 - w*sin(s))/Q(s)
	return atan2(sphi, cphi)

def get_psi(s):
	cpsi = cos(s)/Q(s)
	spsi = (w - sin(s))/Q(s)
	return atan2(spsi, cpsi)

def vecgram(s, phi):
	psi = acos(cos(phi)/w)
	psi = -abs(psi)
	dx2 = w*sin(s+psi)
	dy2 = w*sin(psi)*sin(s) - cos(phi)*cos(s)
	dls = w*sin(psi)*sin(s) - sin(phi)
	return np.array([dy2, dls, dx2])

s = .8*acos(1/w)
vs = []
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for phi in np.linspace(-pi, pi, 50):
	v = vecgram(s, phi)
	vs.append(v)
	print(v)
	ax.plot([0, v[0]], [0, v[1]], [0, v[2]], 'b-')
vs = np.asarray(vs)
ax.plot(vs[:,0], vs[:,1], vs[:,2], 'b-')
ax.set_xlabel('y')
ax.set_ylabel('s')
ax.set_zlabel('x')
	
plt.show()