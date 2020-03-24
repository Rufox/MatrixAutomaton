import Var as var
import numpy as np
#from mendeleev import element
#def gestorMutacion:
#def gestorRecombinacion:

def createRandomPlane():
	v1 = np.random.ranf(3)*2 -1
	v2 = np.random.ranf(3)*2 -1
	#print "VECTORES DEL PLANO"
	#print "0",v1[0],v1[1],v1[2]
	#print "0",	v2[0],v2[1],v2[2]
	plane = (v1[1]* v2[2] - v1[2] * v2[1],
			v1[2]* v2[0] - v1[0] * v2[2],
			v1[0]* v2[1] - v1[1] * v2[0])
	return plane

def rotarMolecula(coordsSist):
	cordinates = np.array([[row[1], row[2], row[3]] for row in coordsSist])
	alhpa, beta, gamma = np.random.randint(0,360),np.random.randint(0,360),np.random.randint(0,360)
	matrix_z= np.array([[np.cos(alhpa),np.sin(alhpa),0],[-np.sin(alhpa),np.cos(alhpa),0],[0,0,1]])
	matrix_x= np.array([[1,0,0],[0,np.cos(beta),np.sin(beta),],[0,-np.sin(beta),np.cos(beta)]])
	matrix_z2= np.array([[np.cos(gamma),np.sin(gamma),0],[-np.sin(gamma),np.cos(gamma),0],[0,0,1]])
	#print matrix_z, matrix_x, matrix_z2
	final = cordinates.dot(matrix_z.dot(matrix_x.dot(matrix_z2)))
	#print "ACA PARTE"
	for i in range(len(coordsSist)):
		#print coordsSist[i][0], final[i][0],final[i][1],final[i][2]
		coordsSist[i][1] = final[i][0]
		coordsSist[i][2] = final[i][1]
		coordsSist[i][3] = final[i][2]
		#print coordsSist[i][0], coordsSist[i][1],coordsSist[i][2],coordsSist[i][3]
	return coordsSist

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

def posicionEnPlano(plane, coordsSist):
	#plane = (0 ,1 ,0)
	#arrayDistancia = []
	#print "Plano es ",plane
	for atom in coordsSist:
		ubicacion = atom[1],atom[2],atom[3]
		#print ubicacion
		#print np.dot(plane,ubicacion)
		atom.append(np.dot(plane,ubicacion))
		#arrayDistancia.append(np.dot(plane,ubicacion))
	coordsSist.sort(key = lambda coordsSist: coordsSist[5])  
	# print "PLANO"
	# print "X",plane[0],plane[1],plane[2]
	# aux=0
	# for j in range(0,9):
	# 	for i in coordsSist:
	# 	# 	if(i[5]>0):
	#  		print i[0],i[1],i[2],i[3]#,i[5]
	#  		aux+=1
	#  		if aux>=j:
	#  			print j+4,"\ns"
	#  			aux=0
	#  			break

	#print "BELOW"
	
	for i in coordsSist:
	# 	if(i[5]<0):
	 	#print (i[0],i[1],i[2],i[3])
	 	i.pop()						# Elimina valor porducto punto
	 	#print i
	
	print "\n"
	return coordsSist

def combinarMolecula(sistema_1, sistema_2, hashTotal):
	
	#Negativo primero
	sistema_2.reverse()
	listaCombinada = sum(zip(sistema_1,sistema_2),())
	verificador = dict.fromkeys(hashTotal,0)
	
	finalCoords = []
	for i in range(0,hashTotal["all"]*2):
		if( verificador[listaCombinada[i][0]] < hashTotal[listaCombinada[i][0]]):
			#print "Atomo: ",listaCombinada[i][0],"Hay ",verificador[listaCombinada[i][0]] ,"<", hashTotal[listaCombinada[i][0]],"Se necesita"
			finalCoords.append(listaCombinada[i])
			verificador[listaCombinada[i][0]]+=1
			verificador["all"]+=1
			#print i
			if verificador["all"] == hashTotal["all"] :
				return finalCoords
	
def mutacionMovimientoAleatorio(cordinates):
	#print cordinates
	#dt = np.dtype([('value',np.unicode_,16),('x',np.float64),('y',np.float64),('z',np.float64),('natom',np.int_)])
	#dt = np.dtype([('name', np.unicode_, 16), ('grades', np.float64, (2,))])
	###[('name', '<U16'), ('grades', '<f8', (2,))]
	#x = np.array([('Sarah', (-0.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
	#print x
	work = np.asarray(cordinates)#,dtype=dt)
	#print type(work)
	#print work.dtype
	#print dt
	#work = np.array([["H", 3.2, 33.2, 0.2, 1]],dtype =dt)
	np.random.shuffle(work)
	#print work
	for i in range(0, int(round(len(work)*var.PcentAtomosMutadosMovimiento))):
		radii = var.atomic_radii[var.atomic_number[(int(work[i][4]))-1]]
		patada_X = radii *np.random.randint(0,21)/10.0 - radii
		patada_Y = radii *np.random.randint(0,21)/10.0 - radii
		patada_Z = radii *np.random.randint(0,21)/10.0 - radii
		#work[i][1]+=patada_X
		#print patada_X,patada_Y,patada_Z
		work[i][1] = float(work[i][1]) + patada_X
		work[i][2]= float(work[i][2]) + patada_Y
		work[i][3]= float(work[i][3]) + patada_Z
		#print work[i]
		#exit(0)
		#print cordinates[i], radii ,patada_X, patada_Y, patada_Z

	return work

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

