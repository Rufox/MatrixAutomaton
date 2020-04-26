
import Lector
import Impresora
import Var as var
import Genetic
import Lanzador as go
import MatrixAutomaton as Mat

import numpy as np
import math
import sys
import time

# Caso especial cuando los atomos vienen en formato de numero atomico.
def transformarNumeroASimbolo(coords):
	nuevo=coords
	for line in nuevo:
		#si es numero
		line.append(line[0])
		line[0]=var.atomic_number[line[0]-1]
	nuevo=[coords,nuevo]
	return nuevo

# Cola a enviar
queue = sys.argv[2]

# Inicializacion de variables globales
var.init()
# Verificacion y elminacion de archivos innecesarios (otras pruebas)
#Impresora.crearArchivos()
# Lectura de archivo de configuracion
Lector.leerArchivoParametros(sys.argv[1])


#print (list(var.Big_variable))

# Inicializaicon de variables locales
convergenciaObtenida = 0
calculosterminados = 1 
hashtotal = var.formulaQuimicaAHash()
generation = 0
MinEnergyEver = 0

#Impresion LOG
Impresora.escribirArchivoLog("Iniciado el programa")
# Ciclo principal de vida, funciona mientras se alcance un nivel de energia constante en un numero de ciclos
while (var.maxConvergencia != convergenciaObtenida):
	
	sistemasNombre = []
	sistemasLanzar = []
	lines = []
	# ZONA 1
	# Creacion de inputs: 
	# 1 MatrixAutomaton, 2 Recombinacion, 3 Mutacion
	
	#Caso especial ciclo 0
	if calculosterminados != 0:
		fitness = []
		coords = []
		energia = []
		mutados = 0
		cruzados = 0
		nuevos = var.Big_variable["numb_conf"]  #CHANGE
		#lines = [1,1,1,1,1,1,1,1,1,1] #CHANGE
		#sistemasNombre = ["job01","Child1_24","job03","job04","job05", #CHANGE
		#		"job06","job07","job08","job02","Child1_23"]#,#"job11"]

	# Ciclos 2+
	else:
		mutados = int(hashtotal["all"])#int(round(var.PcentToMutate * float(var.Big_variable["numb_conf"])))
		cruzados = int(len(indexsAboveCurfew))#int(round(var.PcentToRecombine * float(var.Big_variable["numb_conf"])))
		nuevos =  int(var.Big_variable["numb_conf"]) - mutados -cruzados #CHANGE

	# Matrix Automaton
	if nuevos > 0:
		test = Mat.Llamar(int(nuevos))
		print "\nEsto Es lo que entrega el programa de MATRICES:\n"
		for primer in test:
			print primer
			aux = 0
			for i in primer:
				#print i
				j=i.split(" ")
				primer[aux] = j
				#print j
				aux+=1
			sistemasLanzar.append(primer)
			sistemasNombre.append("Original"+str(generation)+"_")
		print "\n",test
##########################################
	# CROSSING OVER
	if cruzados != 0:
		for Crossing in range(0, cruzados):
			np.random.shuffle(indexsAboveCurfew)
			plano = Genetic.createRandomPlane()
			Genetic.posicionEnPlano(plano,coords[indexsAboveCurfew[0]])
			Genetic.posicionEnPlano(plano,coords[indexsAboveCurfew[1]])
			finalCoords= Genetic.combinarMolecula(coords[indexsAboveCurfew[0]],coords[indexsAboveCurfew[1]],hashtotal)
			sistemasLanzar.append(finalCoords)
			sistemasNombre.append("Child"+str(generation)+"_")
			pass

	# MUTACIONES 0.2 y 0.2 de cualquiera de los alpha
	if mutados != 0:
		for muting in range(0 ,mutados/2):
			np.random.shuffle(indexsAboveCurfew)
			# Muta el primero con dezplazamiento, muta el ultimo con intercambio
			mutDesp = Genetic.mutacionMovimientoAleatorio(coords[indexsAboveCurfew[0]])
			mutInt = Genetic.mutacionIntercambio(coords[indexsAboveCurfew[-1]])
			sistemasNombre.append("MutD"+str(generation)+"_")
			sistemasLanzar.append(mutDesp)
			sistemasNombre.append("MutI"+str(generation)+"_")
			sistemasLanzar.append(mutInt)
#####################################

	#ZONA 2
	# Formacion de inputs en formato gaussian u otro programa
	for iden in range(len(sistemasLanzar)):
		Impresora.escribirInputGaussian(sistemasNombre[iden],iden,sistemasLanzar[iden])
		sistemasNombre[iden]=sistemasNombre[iden]+str(iden)
		# Impresion data
		Impresora.escribirArchivoXYZ("PreCoords_"+str(generation),hashtotal["all"],sistemasNombre[iden],sistemasLanzar[iden])

#####################################
	# Zona 3
	# Envio de input a programa de calculo
	for iden in range(len(sistemasLanzar)):
		go.envioCluster(var.GaussianCall,sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
		lines.append(1)
	#pass
	toKick = []
	while True and len(sistemasLanzar):
		for i in range(len(sistemasLanzar)):
			if lines[i] != 0:
				lines[i] = Lector.obtenerTermination(sistemasNombre[i]+"."+var.extension)

		if(1 in lines):
			print lines
			time.sleep(10.0)
		elif (2 in lines):
			print "Casos erroneos"
			time.sleep(5.0)
			for i in range(len(sistemasLanzar)):
				if (lines[i] == 2):
					if(Lector.obtenerEnergiaGaussian(sistemasNombre[i]+"."+var.extension)!=0):
						lines[i]=0
						continue
					else:
						print "Malos sera: ",sistemasNombre[i]
						go.envioCluster(var.GaussianCall,sistemasNombre[i],sistemasNombre[i]+".com",var.Big_variable["core"],queue)
						print "Enviado"
						lines[i] = 1
					print lines
			time.sleep(20.0)
					# Deben ser eliminados los incorrectos para funcoina bien.
		elif (3 in lines):
			# Atomos muy cercas 1 con otros ... eliminados
			for i in range(len(sistemasLanzar)):
				if (lines[i] == 3):
					print "Eliminando a uno:",sistemasNombre[i]
					#sistemasNombre.remove(sistemasNombre[i])
					toKick.append(i)
					lines[i]=0
		else:
			break
		pass
	#print sistemasLanzar
	#print sistemasNombre
	#print lines
	#print toKick
	toKick.reverse()
	for i in toKick:
		del sistemasNombre[i]
	#print sistemasNombre
	#exit(1)
	# Envio de inputs al programa necesario, espera a termino correcto de calculo
#####################################
	#Zona 4
	# Recopilacion de datos.
	del fitness[:]
	del coords[:]
	del energia[:]
		
	for file in sistemasNombre:
		#if file not in toKick:
		tmp = Lector.obtenerCoordenadaGaussian(file+"."+var.extension)
		energy= float(Lector.obtenerEnergiaGaussian(file+"."+var.extension))
		transformarNumeroASimbolo(tmp)
		coords.append(tmp)
		energia.append(energy)
		#else:
		#	sistemasNombre.remove(file)
######################################
	#ZOna 5
	# distribucion de la energia, cual es el mejor, contador del minimo global actual
	energiaMenor = min(energia)
	energiaMayor = max(energia)
	difEner = energiaMayor - energiaMenor

	for energy in energia:
		prob = (energy - energiaMenor) / difEner
		tmp_fit = math.exp(-prob * var.alphaNumber) 
		fitness.append(tmp_fit)
	sortedIndexs = np.argsort(fitness)
	aux = 0
	index=[]
	for data in sortedIndexs:
		if fitness[data] < var.PcentBestFitness:
			index.append(aux)
		aux+=1
	indexsAboveCurfew = np.delete(sortedIndexs,index)

######################################
	# Zona 6
	# IMPRESION DE COSAS
	for cont in range(len(sistemasNombre)):
		Impresora.escribirArchivoXYZ("PostCoords_"+str(generation),hashtotal["all"],sistemasNombre[cont]+"\tE = "+str(energia[cont])+" H",coords[cont])
	#
	# Caso del mejor
	if(energia[sortedIndexs[-1]] < MinEnergyEver):
		MinEnergyEver = energia[sortedIndexs[-1]]
		Impresora.escribirArchivoXYZ("01FinalsCoords",hashtotal["all"],sistemasNombre[sortedIndexs[-1]]+"\tE = "+str(energia[sortedIndexs[-1]])+" H",coords[sortedIndexs[-1]])
		convergenciaObtenida = 0
		Impresora.escribirArchivoLog("Nuevo Minimo! -> "+sistemasNombre[sortedIndexs[-1]])
		Impresora.escribirArchivoLog("Energia :"+str(energia[sortedIndexs[-1]])+" H")
	#
	convergenciaObtenida+=1
	Impresora.escribirArchivoLog("Convergencia "+str(convergenciaObtenida)+" de "+str(var.maxConvergencia))
	calculosterminados = 0
	
	generation+=1
	del sistemasLanzar[:]
	del sistemasNombre[:]
	pass

# exit(0)
