import numpy as np 
import random

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

def almacenarCoord(a,b,c):
	return a,b,c

def buscarVecinos(m,a,b,c):
	equis = [a,a+1,a-1]
	y_griega = [b,b+1,b-1]
	zeta = [c,c+1,c-1]
	for i in equis:
		for j in y_griega:
			for k in zeta:
				if a == i and b == j and c == k:
					pass
				elif i < 0 or i > 6 or j < 0 or j > 6 or k < 0 or k > 3:
					pass
				elif almacenarCoord(i,j,k) not in lista:
					lista.append(almacenarCoord(i,j,k))				
	return lista

def escogerVecinos():
	global vecino_escogido

	vecino_escogido = random.choice(lista)
	if vecino_escogido in franja:
		pass
	else:
		franja.append(almacenarCoord(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2]))
		matriz[(vecino_escogido[2],vecino_escogido[1],vecino_escogido[0])] = elementos.pop()
		if vecino_escogido == "None":
			pass
		else:
			return vecino_escogido

def guardar(fr):
	global n

	f=open ('hola.xyz','a')
	f.write(str(n) +'\nMatrix\n')
	for i in range(len(fr)):
		f.write(str(matriz[fr[i][2],fr[i][1],fr[i][0]])+' '+str(fr[i][0])+' '+str(fr[i][1])+' '+str(fr[i][2])+'\n')
	f.close() 

def main():
	global x
	global y
	global z
	global matriz
	global lista
	global franja
	global elementos 
	global iteraciones
	global n

	lista = []
	franja = []	
	elementitos = []
	el=[]
	num=[]
	final = []
	n = 6
	iteraciones = 5

	f=open ('hola.xyz','w+')                 # Declare an empty list named mylines.
	
	with open ('Config.in', 'rt') as Config: 
	    for lineas in Config:
	    	if 'chemical_formula' in lineas:
	    		chemical_formula = lineas
	    		elementitos = chemical_formula.split()
	    		elementitos.remove("chemical_formula")
	    		elementitos.remove("=")
	    		for i in elementitos:
	    			if i.isdigit():
	    				num.append(i)
	    			else:
	    				el.append(i+' ')
	    		
	    		for j in range(len(el)):
					final.append(el[j]*int(num[j]))


	while iteraciones > 0:
		elementos = ["Be","Be","N","N","N","C"]
		elementos.reverse()

		matriz = np.zeros(196, dtype = object).reshape(4,7,7)        # 3d array
		
		#eleccion de posicion random para primer elemento
		indices =  np.random.randint(0, high=3, size=3)
		x=indices[0]
		y=indices[1]
		z=random.randint(0,3)

		print "Coordenadas generadas para primer atomo ( x:",x,", y:",y,", z:",z,")"

		#Estoy descubriendo como trabajar con las clases D: sdkfnjksdf
		raiz = Nodo(None,x,y,z,0)
		nodo_activo = raiz

		franja.append(almacenarCoord(x,y,z))

		matriz[(z,y,x)] = elementos.pop()
		#print "Coordenadas de atomo agregado a la franja de solucion: ", franja
		#print matriz
		#print "Sus posibles vecinos (x,y,z):\n",
		buscarVecinos(matriz,x,y,z)
		#print "Coordenadas del vecino escogido aleatoriamente (x,y):", 
		escogerVecinos()
		#print "Coordenadas de atomos agregados a la franja de solucion: ", franja
		#print matriz				

		while len(franja) < n:

			#print "Coordenadas del vecino escogido aleatoriamente (x,y):", 
			escogerVecinos()
			#print "Sus posibles vecinos (x,y,z):\n",
			buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
			#print matriz
			#print "Atomos agregados a la franja de solucion: ", franja
			
		iteraciones = iteraciones - 1
		guardar(franja)
		print matriz
		matriz = matriz*0
		
		franja = []
		lista = []

if __name__=="__main__":
    main();