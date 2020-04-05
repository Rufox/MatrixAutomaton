import Var as var
import numpy as np

# Formula plano, crea 2 vectores aleatorios y forma plano que pasa por punto 0,0,0
def createRandomPlane():
	v1 = np.random.ranf(3)*2 -1
	v2 = np.random.ranf(3)*2 -1
	plane = (v1[1]* v2[2] - v1[2] * v2[1],
			v1[2]* v2[0] - v1[0] * v2[2],
			v1[0]* v2[1] - v1[1] * v2[0])
	return plane

# Rota un sistemas de coordenadas por medio del triple movimiento ZXZ.
# Los angulos (alpha, beta, gama) de movimiento son aleatorios
def rotarMolecula(coordsSist):
	cordinates = np.array([[row[1], row[2], row[3]] for row in coordsSist])
	alhpa, beta, gamma = np.random.randint(0,360),np.random.randint(0,360),np.random.randint(0,360)
	matrix_z= np.array([[np.cos(alhpa),np.sin(alhpa),0],[-np.sin(alhpa),np.cos(alhpa),0],[0,0,1]])
	matrix_x= np.array([[1,0,0],[0,np.cos(beta),np.sin(beta)],[0,-np.sin(beta),np.cos(beta)]])
	matrix_z2= np.array([[np.cos(gamma),np.sin(gamma),0],[-np.sin(gamma),np.cos(gamma),0],[0,0,1]])
	final = cordinates.dot(matrix_z.dot(matrix_x.dot(matrix_z2)))
	for i in range(len(coordsSist)):	# eliminacion de np.array
		coordsSist[i][1] = final[i][0]
		coordsSist[i][2] = final[i][1]
		coordsSist[i][3] = final[i][2]
	return coordsSist					# retorna sistema de coordenadas en arreglo.

def centrarMolecula(coordsSist):
	#Centro de masa: (Masa MOl x Coordenadas)/Masa Total
	sum_x,sum_y,sum_z=0,0,0
	peso= 0
	for atomos in coordsSist:
		peso+=var.elementsWeight[atomos[4]-1]
		sum_x+=var.elementsWeight[atomos[4]-1]*atomos[1]
		sum_y+=var.elementsWeight[atomos[4]-1]*atomos[2]
		sum_z+=var.elementsWeight[atomos[4]-1]*atomos[3]
	center = '',sum_x/peso, sum_y/peso, sum_z/peso,0
	for atomos in coordsSist:
		for i in range(1 ,	3):
			atomos[i] -=center[i]
	return coordsSist

# ordena los producto punto de cada coordenada en el sistema contra el plano.
# en palabras simples: Que tan lejos esta el punto del plano?
def posicionEnPlano(plane, coordsSist):
	for atom in coordsSist:
		ubicacion = atom[1],atom[2],atom[3]
		atom.append(np.dot(plane,ubicacion))
	coordsSist.sort(key = lambda coordsSist: coordsSist[5])  
	
	for i in coordsSist:
	 	i.pop()						# Elimina valor porducto punto
	return coordsSist

def combinarMolecula(sistema_1, sistema_2, hashTotal):
	
	#Negativo primero
	sistema_2.reverse()
	listaCombinada = sum(zip(sistema_1,sistema_2),())  #Combinacion intercalada de ambos sistemas
	verificador = dict.fromkeys(hashTotal,0)
	
	finalCoords = []
	for i in range(0,hashTotal["all"]*2):
		if( verificador[listaCombinada[i][0]] < hashTotal[listaCombinada[i][0]]):  #Verifica cada atomo
			finalCoords.append(listaCombinada[i])
			verificador[listaCombinada[i][0]]+=1
			verificador["all"]+=1
			if verificador["all"] == hashTotal["all"] :								# Todos los atomos han sido posicionados
				return finalCoords

# Cada atomos sufre una traslacion en x, y, z (diferentes)
# se mutan x% de las coordenadas. Valor especificado en Var.py
# Todo se mueve hasta 1A 
def mutacionMovimientoAleatorio(cordinates):
	work = np.asarray(cordinates)
	np.random.shuffle(work)
	for i in range(0, int(round(len(work)*var.PcentAtomosMutadosMovimiento))):
		radii = var.atomic_radii[var.atomic_number[(int(work[i][4]))-1]]
		patada_X = radii *np.random.randint(0,21)/10.0 - radii
		patada_Y = radii *np.random.randint(0,21)/10.0 - radii
		patada_Z = radii *np.random.randint(0,21)/10.0 - radii
		work[i][1] = float(work[i][1]) + patada_X
		work[i][2]= float(work[i][2]) + patada_Y
		work[i][3]= float(work[i][3]) + patada_Z
	return work

# Todos los atomos son intercambiados aleatoriamente.
def mutacionIntercambio(cordinates):
	work = np.asarray(cordinates)
	np.random.shuffle(work)
	#print cordinates,"\n"
	primero, ultimo = work[0][0], work[0][-1]
	for i in range(0,len(work)-1):
		work[i][0], work[i][-1] = work[i+1][0], work[i+1][-1]
	
	work[-1][0], work[-1][-1] = primero, ultimo
	return work
	#print cambiado

