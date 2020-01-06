import numpy as np 
import random

#Para leer inputs txt

with open("hola.txt", "r+") as f:
	data = f.readlines()
 
	for line in data:
		#split para separar archivo por palabras
		words = line.split()
		print words

# archivo = open("hola.txt", "r+")
# for linea in archivo.readlines():
# 	print linea

# archivo.write("Hola") 
# archivo.close() 


#class Atomo:

#class Cluster:

class Nodo:
	def __init__(self, padre, profundidad):
		self.padre = padre
		self.hijo = []
		self.profundidad = profundidad

# 	def agregarHijo(self, hijo):
# 		self.hijo.append(hijo)

# 	def tieneHijo(self):
# 		return len(self.hijo) > 0
	
# 	def obtenerHijo(self):
# 		return self.hijo

# 	def obtenerPadre(self):
# 		return self.padre

# 	def obtenerProfundidad(self):
# 		return self.profundidad

# 	def __str__(self):
# 		return str(self.franja)

# raiz = Nodo(None,0)
# franja = []
# nodoActivo = raiz
# franja.append(nodoActivo)
# print franja


                     #reshape(set de numeros, eje x, eje y)
matriz = np.zeros(48, dtype = object).reshape(3,4,4)        # 3d array

#eleccion de posicion random para primer elemento
indices =  np.random.randint(0, high=3, size=3)

x=indices[0]
y=indices[1]
z=random.randint(0,2)

print "Coordenadas generadas para primer atomo (z:",z,", x:",x,", y:",y,")"

def asignar(m,a,b,c):
	#(z,x,y)=(set [0/2], eje x, eje y)
	m[(c,b,a)]=1

asignar(matriz,x,y,z)

def obtenerCoordenadas():
	for i in range(4):
		if matriz[(z,y,i)] == 1:
			col = i;
		for j in range(4):
			if matriz[(z,j,x)] == 1:
				fila= j;
	return col,fila
#obtenerCoordenadas()

def almacenarCoord(a,b):
	return a,b

#m: matriz, a: coord eje x, b: coord eje y, c: coord eje z
def buscarVecinos(m,a,b,c):
	
	global lista
	lista =[]
	if m[(c,b,a-1)] == 0:
		asignar(m,a-1,b,c)
		lista.append(almacenarCoord(a-1,b))
		if m[(c,b-1,a-1)] == 0:
			asignar(m,a-1,b-1,c)
			lista.append(almacenarCoord(a-1,b-1))
			if m[(c,b-1,a)] == 0:
				asignar(m,a,y-1,z)
				lista.append(almacenarCoord(a,b-1))
				if m[(c,b-1,a+1)] == 0:
					asignar(m,a+1,b-1,c)
					lista.append(almacenarCoord(a+1,b-1))
					if m[(c,b,a+1)] == 0:
						asignar(m,a+1,b,c)
						lista.append(almacenarCoord(a+1,b))
						if m[(c,b+1,a+1)] == 0:
							asignar(m,a+1,b+1,c)
							lista.append(almacenarCoord(a+1,b+1))
							if m[(c,b+1,a)] == 0:
								asignar(m,a,b+1,c)
								lista.append(almacenarCoord(a,b+1))
								if m[(c,b+1,a-1)] == 0:
									asignar(m,a-1,b+1,c)
									lista.append(almacenarCoord(a-1,b+1))
									m[(c,b,a)] = 0
	return lista

def escogerVecinos():
	global vecinoEscogido
	global lista
	global franja
	vecinoEscogido = random.choice(lista)
	matriz[(z,vecinoEscogido[1],vecinoEscogido[0])] = "O"
	franja.append(almacenarCoord(vecinoEscogido[0],vecinoEscogido[1]))
	return vecinoEscogido

# holis = np.where(matriz>0)
# print holis
# print matriz[holis]

# for index, x in np.ndenumerate(matriz):
#     print(index, x)

print "Sus posibles vecinos (x,y):\n",buscarVecinos(matriz,x,y,z)

matriz = matriz*0

franja = []
franja.append(almacenarCoord(x,y))

matriz[(z,y,x)] = "H"
print "Atomos agregados a la franja de solucion: ", franja
print matriz
print "Coordenadas del vecino escogido (x,y):", escogerVecinos()
print matriz
copia = matriz.copy()
print "Atomos agregados a la franja de solucion: ", franja


n = 5
while len(franja) < n:
	print "Posibles vecinos para el siguiente atomo: ", buscarVecinos(copia,vecinoEscogido[0],vecinoEscogido[1],z)
	print "Coordenadas del vecino escogido (x,y):", escogerVecinos()
	print matriz
	print "Atomos agregados a la franja de solucion: ", franja
