# Here we write some functions that help us analayze the motions of a rigid body

# import the required modules
import math
import numpy as np

def rot_2d(theta):
	"""
	Receives an input in radians and
	returns a 2D rotation matrix
	R = [cos(theta) -sin(theta)
	     sin(theta)  cos(theta)]
	"""
	rot = np.array([[math.cos(theta), -math.sin(theta)],
					[math.sin(theta), math.cos(theta)]])
	return rot
