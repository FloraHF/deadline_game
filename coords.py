import numpy as np
from math import atan2

def get_s(xP, xE):
	PE = np.concatenate(xE - xP, [0])
	yaxis = np.array([0, -1, 0])
	s = atan2(np.cross(yaxis, PE)[-1], np.dot(yaxis, PE))