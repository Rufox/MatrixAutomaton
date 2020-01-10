import Var as var
import numpy as np




#def gestorMutacion:
#def gestorRecombinacion:

def createRandomPlane():
	plane = np.random.ranf(2)*2 -1
	print ("ranndom sera:",plane)
	plane =np.append(plane,0)
	print ("ranndom sera:",plane)
	return plane

#def centrarMolecula(coordsSist):
def rotarMolecula(coordsSist):
	axis = np.random.random(3)*2-1
	rot_axis = np.append([0.0],axis)
	theta = np.random.ranf(1)*2-1
	axis_angle = (theta*0.5) * rot_axis/np.linalg.norm(rot_axis)

	print (axis_angle)
