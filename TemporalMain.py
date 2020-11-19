
import Lector
import Impresora
import Var as var
import Genetic
import Lanzador as go
import MatrixAutomaton as Mat

import numpy as np
import os,glob
import math
import sys
import time
from datetime import datetime


# Caso especial cuando los atomos vienen en formato de numero atomico.
def transformarNumeroASimbolo(coords):
	nuevo=coords
	for line in nuevo:
		#si es numero
		line.append(line[0])
		line[0]=var.atomic_number[line[0]-1]
	nuevo=[coords,nuevo]
	return nuevo
def GestorEnvio(sistemasNombre,queue,iden,reset):
	if(var.Big_variable["job-scheduler"].lower()=="local"):
		#modo local
		LANZ = int(math.ceil((iden)/var.bloque))
		LANZ_Futuro = int(math.ceil((iden+1)/var.bloque))
		print("LANZ = ",LANZ, iden,var.bloque)
		go.LocalMode(str(reset),sistemasNombre[iden]+"."+var.software_extensions[var.Big_variable["software"].lower()], LANZ)
		
		if ((LANZ_Futuro != LANZ or (iden+1)==int(var.Big_variable["numb_conf"])) and reset==0) :
			print("Se envia el BATCH",LANZ)
			go.SendLocal(str(reset),LANZ)
		elif(reset!=0):
			return 4
		elif(reset!=0 and iden==-1): #Procede a tirar todos los BACTH
			for i in range(0,var.bloque):
				go.SendLocal(str(reset),i)
				pass
		#	print("Estamos en reset: ",reset)
		#	go.SendLocal(str(reset),LANZ)
		#	aux=0
		#	time.sleep(2)
	elif(var.Big_variable["job-scheduler"].lower()=="slurm"):
		go.slurmCluster(sistemasNombre[iden],sistemasNombre[iden]+"."+var.software_extensions[var.Big_variable["software"].lower()],var.Big_variable["core"],queue)
		return 1
	elif(var.Big_variable["job-scheduler"].lower()=="sge"):
		go.SGECluster(sistemasNombre[iden],sistemasNombre[iden]+"."+var.software_extensions[var.Big_variable["software"].lower()],var.Big_variable["core"],queue)
		return 1
	else:
		print("Job-Scheduler not recognized.\nAccepted:\nlocal, slurm or sge\n")
		exit(1);
# Cola a enviar


# Inicializacion de variables globales
var.init()
queue = sys.argv[2]
# Verificacion y elminacion de archivos innecesarios (otras pruebas)
#Impresora.crearArchivos()
# Lectura de archivo de configuracion
Lector.leerArchivoParametros(sys.argv[1])



if(var.Big_variable["job-scheduler"]=="local"):
#	print( "LOCAL")
	var.distribucionCalculos()
	#os.remove("*.slrm")
	#print(var.bloque)

#exit(1)
#print (list(var.Big_variable))

# Inicializaicon de variables locales
convergenciaObtenida = 0
calculosterminados = 1 
hashtotal = var.formulaQuimicaAHash()
generation = 0
MinEnergyEver = 0
reset = False
tiempo_inicial=datetime.now()

if var.Big_variable["software"] == "orca":
	var.extension = "out"

if var.reset == 1:
	reset=True


#Impresion LOG
if reset == True:
	Impresora.escribirArchivoLog("Reiniciado el programa  @ " + tiempo_inicial.strftime('%d/%m/%Y %H:%M:%S'))   
else:
	Impresora.escribirArchivoLog("Iniciado el programa @ " + tiempo_inicial.strftime('%d/%m/%Y %H:%M:%S'))
# Ciclo principal de vida, funciona mientras se alcance un nivel de energia constante en un numero de ciclos
while (var.maxConvergencia != convergenciaObtenida):
	for filename in glob.glob("BATCH*"):
		print("Eliminacion de Archivos residuales")
		os.remove(filename) 

	sistemasNombre = []
	sistemasLanzar = []
	lines = []
	Opportunities = []
	# ZONA 1
	# Creacion de inputs: 
	# 1 MatrixAutomaton, 2 Recombinacion, 3 Mutacion
	
	#Caso especial ciclo 0
	if calculosterminados != 0:
		if reset == True:
			# Coords = Simbolo X Y Z NumAtomic
			generation,convergenciaObtenida,MinEnergyEver,read =Lector.leerLOGS()
			energia, coords =Lector.leerInformacionXYZ(read)
			#print "RESET ",generation,convergenciaObtenida,MinEnergyEver
			#print energia
			mutados = cruzados = nuevos = 0
			fitness = []
		else:
			fitness = []
			coords = []
			energia = []
			mutados = 0
			cruzados = 0
			nuevos = int(var.Big_variable["numb_conf"])  #CHANGE
		#TESTls
		nuevos=0
		lines = [1,1,1,1,1] #CHANGE
		sistemasNombre = ["job01","job11","job21","job31", #CHANGE
			   "job41"]#],"job51"]#,"job08","job02","Child1_23"]#,#"job11"]
		sistemasLanzar=[1,2,3,4,5]


	# Ciclos 2+	
	else:
		print("VOLVIENDO")
		mutados = int(round(var.PcentToMutate * float(var.Big_variable["numb_conf"]))) #int(hashtotal["all"])#
		nuevos =  int(round(var.PcentToCreate * float(var.Big_variable["numb_conf"]))) #int(var.Big_variable["numb_conf"]) - mutados -cruzados #CHANGE
		cruzados = int(var.Big_variable["numb_conf"]) - mutados -nuevos #int(len(indexsAboveCurfew))#int(round(var.PcentToRecombine * float(var.Big_variable["numb_conf"])))
		
	print("NUEVOS SERAN:",nuevos,mutados,cruzados," Original, Mut, Child")
	# Matrix Automaton
	if nuevos > 0:
		pob_1d = int(round(float(nuevos)*var.Pcent1D))
		pob_2d = int(round(float(nuevos)*var.Pcent2D))
		pob_3d = int(nuevos)- pob_1d - pob_2d
		print(pob_1d,pob_2d,pob_3d)
		#exit(1)
		Mat1D = Mat.Llamar(int(pob_1d),1)
		Mat2D = Mat.Llamar(int(pob_2d),2)
		Mat3D = Mat.Llamar(int(pob_3d),3)
		#print "\nEsto Es lo que entrega el programa de MATRICES:\n"
		for primer in Mat1D:
		#   print primer
			aux = 0
			for i in primer:
				#print i
				j=i.split(" ")
				primer[aux] = j
				#print j
				aux+=1
			sistemasLanzar.append(primer)
			sistemasNombre.append("Original1D_"+str(generation)+"_")
		for primer in Mat2D:
		#   print primer
			aux = 0
			for i in primer:
				#print i
				j=i.split(" ")
				primer[aux] = j
				#print j
				aux+=1
			sistemasLanzar.append(primer)
			sistemasNombre.append("Original2D_"+str(generation)+"_")
		for primer in Mat3D:
		#   print primer
			aux = 0
			for i in primer:
				#print i
				j=i.split(" ")
				primer[aux] = j
				#print j
				aux+=1
			sistemasLanzar.append(primer)
			sistemasNombre.append("Original3D_"+str(generation)+"_")
		#print "\n",test
		#exit(1)
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
			sistemasNombre.append("Child_"+str(generation)+"_")
			pass

	# MUTACIONES 0.2 y 0.2 de cualquiera de los alpha
	if mutados != 0:
		for muting in range(0 ,mutados//2):
			np.random.shuffle(indexsAboveCurfew)
			# Muta el primero con dezplazamiento, muta el ultimo con intercambio
			mutDesp = Genetic.mutacionMovimientoAleatorio(coords[indexsAboveCurfew[0]])
			mutInt = Genetic.mutacionIntercambio(coords[indexsAboveCurfew[-1]])
			sistemasNombre.append("MutD_"+str(generation)+"_")
			sistemasLanzar.append(mutDesp)
			sistemasNombre.append("MutI_"+str(generation)+"_")
			sistemasLanzar.append(mutInt)
		if mutados%2 != 0:
			mutDesp = Genetic.mutacionMovimientoAleatorio(coords[indexsAboveCurfew[0]])
			sistemasNombre.append("MutD_"+str(generation)+"_")
			sistemasLanzar.append(mutDesp)
#####################################

	#ZONA 2
	# Formacion de inputs en formato gaussian u otro programa
	print("zona 2")
	if reset == False:
		for iden in range(len(sistemasLanzar)):
			#EDIT no va break
			##Impresora.escribirInput(sistemasNombre[iden],iden,sistemasLanzar[iden])
			##sistemasNombre[iden]=sistemasNombre[iden]+str(iden)
			# Impresion data
			##Impresora.escribirArchivoXYZ("PreCoords_"+str(generation),hashtotal["all"],sistemasNombre[iden],sistemasLanzar[iden])
			break

#####################################
	# Zona 3
	# Envio de input a programa de calculo
	print(sistemasLanzar)
	print(var.maxConvergencia, "MAX CONVGENCIA")
	if reset == False:
		for iden in range(len(sistemasLanzar)):
			#EDIT
			#go.envioCluster(var.GaussianCall,sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
			#go.slurmCluster(sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
			#go.SGECluster(sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
		#	GestorEnvio(sistemasNombre,queue,iden,0)
		#	time.sleep(0.25)
			# Flag estado
		#	lines.append(1)
			# Contador envio calculo
			print("Enviando a lanzar")
			Opportunities.append(1)
		#pass
		toKick = []
		contador=1
		while True and len(sistemasLanzar):
			print ("Oportunidades")
			print (Opportunities)
		
			for i in range(len(sistemasLanzar)):
				if lines[i] != 0 and lines[i]!=4:
					lines[i] = Lector.obtenerTermination(sistemasNombre[i]+"."+var.extension)
			print(lines)
			#if(1 in lines):
			#	print("UNO CORRIENDO")
			#	print(lines)
			#	time.sleep(1.0)
			if (2 in lines):
				print("Casos erroneos")
				time.sleep(1.0)
				for i in range(len(sistemasLanzar)):
					if (lines[i] == 2):
						if(Lector.obtenerEnergia(sistemasNombre[i]+"."+var.extension)!=0):
							print("Existe Energia para:", sistemasNombre[i])
							lines[i]=0
							continue
						elif(Opportunities[i] < var.treshold):
							print("Malos sera: ",sistemasNombre[i])
							#go.envioCluster(var.GaussianCall,sistemasNombre[i],sistemasNombre[i]+".com",var.Big_variable["core"],queue)
							#go.slurmCluster(sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
							#go.SGECluster(sistemasNombre[iden],sistemasNombre[iden]+".com",var.Big_variable["core"],queue)
							lines[i] = GestorEnvio(sistemasNombre,queue,i,contador)
							Opportunities[i]+=1
						else:
							print("Eliminando a uno:",sistemasNombre[i])
							toKick.append(i)
							lines[i]=0
						print(lines)
				time.sleep(2.0)
						# Deben ser eliminados los incorrectos para funcoina bien.
			elif (3 in lines):
				print("Caso especial : 3!!!")
				# Atomos muy cercas 1 con otros ... eliminados
				for i in range(len(sistemasLanzar)):
					if (lines[i] == 3):
						print("Eliminando a uno:",sistemasNombre[i])
						#sistemasNombre.remove(sistemasNombre[i])
						toKick.append(i)
						lines[i]=0
			elif(1 in lines):
				print("Todos son 1")
				time.sleep(1.0)
				break
			elif(4 in lines):
				print("Envio rezagados modo local")
				GestorEnvio(sistemasNombre,queue,-1,contador)
				contador+=1
			else:
				break
			pass
	#print(sistemasLanzar)
	#print sistemasNombre
	#print lines
		toKick.sort()
		toKick.reverse()
		for i in toKick:
			print("Eliminado el ",sistemasNombre[i])
			del sistemasNombre[i]
	#print sistemasNombre
	#exit(1)
	# Envio de inputs al programa necesario, espera a termino correcto de calculo
#####################################
	#Zona 4
	# Recopilacion de datos.
	exit(1)
	if reset == False:
		del fitness[:]
		del coords[:]
		del energia[:]
		for file in sistemasNombre:
			#if file not in toKick:
			tmp = Lector.obtenerCoordenada(file+"."+var.extension)
			print(tmp)
			print(Lector.obtenerEnergia(file+"."+var.extension))
			energy= float(Lector.obtenerEnergia(file+"."+var.extension))
			transformarNumeroASimbolo(tmp)
			coords.append(tmp)
			energia.append(energy)
		#else:
		#   sistemasNombre.remove(file)
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
	if reset == False:
		for cont in range(len(sistemasNombre)):
			Impresora.escribirArchivoXYZ("PostCoords_"+str(generation),hashtotal["all"],sistemasNombre[cont]+"\tE = "+str(energia[cont])+" H",coords[cont])
	#
		# Caso del mejor
		Impresora.escribirArchivoLog("\nCiclo = "+str(generation))  
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
	reset = False
	#print indexsAboveCurfew
	pass

#print "FINALIZADO"
tiempo_final=datetime.now()
Impresora.escribirArchivoLog("\nProceso Finalizado @ " + tiempo_final.strftime('%d/%m/%Y %H:%M:%S'))
# exit(0)
