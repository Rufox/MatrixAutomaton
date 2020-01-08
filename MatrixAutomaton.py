import numpy as np 
import random
import itertools

#class Atomo:

#class Cluster:

class Nodo:
	def __init__(self, padre, x, y, z, profundidad):
		self.padre = padre
		self.x = x
		self.y = y
		self.z = z
		self.hijo = []
		self.profundidad = profundidad

 	def agregarHijo(self, hijo):
		self.hijo.append(hijo)

 	def tieneHijo(self):
 		return len(self.hijo) > 0
	
 	def obtenerHijo(self):
 		return self.hijo

 	def obtenerPadre(self):
 		return self.padre

 	def obtenerProfundidad(self):
 		return self.profundidad

 	def __str__(self):
 		return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z) 
 		#return "Padre:"+ str(self.padre)+", Profundidad:"+ str(self.profundidad)

# raiz = Nodo(None,0)
# franja = []
# nodoActivo = raiz
# franja.append(nodoActivo)
# print franja

def asignar(m,a,b,c):
	#(z,x,y)=(set [0/2], eje x, eje y)
	m[(c,b,a)]=1

def obtenerCoordenadas():
	for i in range(4):
		if matriz[(z,y,i)] == 1:
			col = i;
		for j in range(4):
			if matriz[(z,j,x)] == 1:
				fila= j;
	return col,fila

def almacenarCoord(a,b,c):
	return a,b,c

def buscarVecinos(m,a,b,c):
	equis = [a,a+1,a-1]
	ygriega = [b,b+1,b-1]
	zeta = [c,c+1,c-1]
	for i in equis:
		for j in ygriega:
			for k in zeta:
				if a == i and b == j and c == k:
					pass
				elif i < 0 or i > 3 or j < 0 or j > 3 or k < 0 or k > 2:
					pass
				elif almacenarCoord(i,j,k) not in lista:
					lista.append(almacenarCoord(i,j,k))				
	return lista

#m: matriz, a: coord eje x, b: coord eje y, c: coord eje z
# def buscarVecinos(m,a,b,c):
# 	if m[(c,b,a-1)] == 0 and almacenarCoord(a-1,b) not in lista:
# 		asignar(m,a-1,b,c)
# 		lista.append(almacenarCoord(a-1,b))
# 		if m[(c,b-1,a-1)] == 0 and almacenarCoord(a-1,b-1) not in lista:
# 			asignar(m,a-1,b-1,c)
# 			lista.append(almacenarCoord(a-1,b-1))
# 			if m[(c,b-1,a)] == 0 and almacenarCoord(a,b-1) not in lista:
# 				asignar(m,a,y-1,z)
# 				lista.append(almacenarCoord(a,b-1))
# 				if m[(c,b-1,a+1)] == 0 and almacenarCoord(a+1,b-1) not in lista:
# 					asignar(m,a+1,b-1,c)
# 					lista.append(almacenarCoord(a+1,b-1))
# 					if m[(c,b,a+1)] == 0 and almacenarCoord(a+1,b) not in lista:
# 						asignar(m,a+1,b,c)
# 						lista.append(almacenarCoord(a+1,b))
# 						if m[(c,b+1,a+1)] == 0 and almacenarCoord(a+1,b+1) not in lista:
# 							asignar(m,a+1,b+1,c)
# 							lista.append(almacenarCoord(a+1,b+1))
# 							if m[(c,b+1,a)] == 0 and almacenarCoord(a,b+1) not in lista:
# 								asignar(m,a,b+1,c)
# 								lista.append(almacenarCoord(a,b+1))
# 								if m[(c,b+1,a-1)] == 0 and almacenarCoord(a-1,b+1) not in lista:
# 									asignar(m,a-1,b+1,c)
# 									lista.append(almacenarCoord(a-1,b+1))
# 									m[(c,b,a)] = 0
# 	return lista

def escogerVecinos():
	global vecino_escogido

	vecino_escogido = random.choice(lista)
	
	if vecino_escogido not in franja:
		franja.append(almacenarCoord(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2]))
		matriz[(vecino_escogido[2],vecino_escogido[1],vecino_escogido[0])] = elementos.pop()
		if vecino_escogido != "None":
			return vecino_escogido

def main():
	global x
	global y
	global z
	global franja
	global matriz
	global lista
	global elementos 
	lista = []
	franja = []	
	elementos = ["C","N","N","N","Be","Be"]
	
	
	#Para leer inputs txt
	# with open("hola.txt", "r+") as f:
	# 	data = f.readlines()
	 
	# 	for line in data:
	# 		#split para separar archivo por palabras
	# 		words = line.split()
	# 		print words

                     #reshape(set de numeros, eje x, eje y) 
	matriz = np.zeros(48, dtype = object).reshape(3,4,4)        # 3d array

	#eleccion de posicion random para primer elemento
	indices =  np.random.randint(0, high=3, size=3)

	x=indices[0]
	y=indices[1]
	z=random.randint(0,2)



	print "Coordenadas generadas para primer atomo ( x:",x,", y:",y,", z:",z,")"
	asignar(matriz,x,y,z)

	#Estoy descubriendo como trabajar con las clases D: sdkfnjksdf
	raiz = Nodo(None,x,y,z,0)
	nodo_activo = raiz

	#print nodo_activo

	franja.append(almacenarCoord(x,y,z))

	matriz[(z,y,x)] = elementos.pop()
	print "Coordenadas de atomo agregado a la franja de solucion: ", franja
	print matriz
	print "Sus posibles vecinos (x,y,z):\n",buscarVecinos(matriz,x,y,z)
	print "Coordenadas del vecino escogido aleatoriamente (x,y):", escogerVecinos()

	print "Coordenadas de atomos agregados a la franja de solucion: ", franja
	print matriz
	
	n = 6
	while len(franja) < n:

		print "Coordenadas del vecino escogido aleatoriamente (x,y):", escogerVecinos()
	
		print "Sus posibles vecinos (x,y,z):\n",buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
		print matriz
		print "Atomos agregados a la franja de solucion: ", franja

    
if __name__=="__main__":
    main();