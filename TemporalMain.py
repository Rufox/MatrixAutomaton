
import Lector
import Impresora
import Var as var
import Genetic
import numpy as np
import math
def transformarNumeroASimbolo(coords):
	nuevo=coords
	#print (var.atomic_number[2])
	for line in nuevo:
		#si es numero
		line.append(line[0])
		line[0]=var.atomic_number[line[0]-1]
	nuevo=[coords,nuevo]
	return nuevo
		

var.init()
Lector.leerArchivoParametros()


print (list(var.Big_variable))

#Llamado programa isisdora, se obtiene algo

# Primer ciclo indica si se encontro el mejor
# Sea la variable convergenciaObtenida la medidora de ello.
# Sea maxConvergencia aquella establecida como quiebre.


# automata, mutados, combinados

convergenciaObtenida = 0
calculosterminados = 1 
hashtotal = var.formulaQuimicaAHash()
#print hashtotal

generation = 0
while (var.maxConvergencia != convergenciaObtenida):
	
	sistemasNombre = []
	sistemasLanzar = []
	# mutados = var.PcentToMutate * 
	# ZONA 1
	# Creacion de inputs: 
	# 1 isidora, 2 genetic, 3 mutacion
	
	if calculosterminados != 0:
		fitness = []
		coords = []
		energia = []
		mutados = 0
		cruzados = 0
		nuevos = 0#var.Big_variable["numb_conf"]  #CHANGE
		sistemasNombre = ["job01","job02","job03","job04","job05", #CHANGE
				"job06","job07","job08","job09","job10","job11"]
	else:
		print "SEEGUNDA BUELTAs"
		mutados = int(round(var.PcentToMutate * float(var.Big_variable["numb_conf"])))
		cruzados = int(round(var.PcentToRecombine * float(var.Big_variable["numb_conf"])))
		nuevos = 0 # total - mutados -cruzados CHANGE

##########################################
	# CROSSING OVER
	if cruzados != 0:
		for Crossing in xrange(len(indexsAboveCurfew)):
			#print Crossing
			np.random.shuffle(indexsAboveCurfew)
			#print indexsAboveCurfew
			plano = Genetic.createRandomPlane()
			#print coords[indexsAboveCurfew[0]]
			Genetic.posicionEnPlano(plano,coords[indexsAboveCurfew[0]])
			#print coords[indexsAboveCurfew[0]]
			Genetic.posicionEnPlano(plano,coords[indexsAboveCurfew[1]])
			finalCoords= Genetic.combinarMolecula(coords[indexsAboveCurfew[0]],coords[indexsAboveCurfew[1]],hashtotal)
			sistemasLanzar.append(finalCoords)
			sistemasNombre.append("Child"+str(generation)+"_")
			#for i in finalCoords:
			#	print i[4],i[1],i[2],i[3]

			pass
	# MUTACIONES 0.2 y 0.2 de cualquiera de los alpha
	if mutados != 0:
		print "HAPENS"
		for muting in range(0 ,mutados):
			#print muting
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
#####################################
	# Zona 3
	# Envio de inputs al programa necesario, espera a termino correcto de calculo
#####################################
	#Zona 4
	# Recopilacion de datos.

	for file in sistemasNombre:
		tmp = Lector.obtenerCoordenadaGaussian(file+".out")
		energy= float(Lector.obtenerEnergiaGaussian(file+".out"))
		print file ," esto da ", energy
		transformarNumeroASimbolo(tmp)
		#print tmp
		coords.append(tmp)
		energia.append(energy)
	#for x in xrange(len(coords)):
	#	print energia[x]
		#for i in coords[x]:
		#	print i
	#	pass
######################################
	#ZOna 5
	# distribucion de la energia, cual es el mejor, contador del minimo global actual
	#esto sale en la linea 3398
	energiaMenor = min(energia)
	energiaMayor = max(energia)
	difEner = energiaMayor - energiaMenor

	for energy in energia:
		prob = (energy - energiaMenor) / difEner
		print energy," -> " ,prob
		tmp_fit = math.exp(-prob * var.alphaNumber) 
		fitness.append(tmp_fit)
	#for w in fitness:
	#	print w
	sortedIndexs = np.argsort(fitness)
	aux = 0
	index=[]
	for data in sortedIndexs:
		if fitness[data] < var.PcentBestFitness:
			#print "PASO", fitness[data] , data
			index.append(aux)
		aux+=1
	#print index
	print sortedIndexs
	indexsAboveCurfew = np.delete(sortedIndexs,index)
	#print indexsAboveCurfew
	#print energia
	#print fitness[sortedIndexs]
	#for x in fitness[sortedIndexs]:
	#	print x
	#	pass
	# Nuemro final que pasan a siguiente vuelta.

	# IMPRESION DE COSAS
	convergenciaObtenida+=1
	calculosterminados = 0
	#exit(0)
	#print convergenciaObtenida
	generation+=1
	pass

exit(0)


































print (var.Big_variable["numb_conf"])
love=[['Ge',      -0.333821000 ,     1.303262000  ,    2.341189000,32],
['Sn' ,      2.730896000 ,     0.020517000 ,  -0.840340000,50],
['Bi'  ,    -1.764684000 ,     1.508150000  ,   -0.128406000,83],
['Sn'  ,     1.156037000 ,    -2.280837000  ,    0.182246000,50],
['Sn'  ,     1.146004000 ,     2.296151000  ,    0.230184000,50],
['Bi'  ,     0.022383000 ,    -0.025529000  ,   -2.058139000,83],
['Ge'  ,    -0.299796000 ,    -1.337354000  ,    2.353758000,32],
['Ge'  ,    1.885563000 ,     0.001446000  ,    1.853211000,32],
['Bi'  ,    -1.772267000 ,    -1.491619000  ,   -0.080269000,83]]

love2=[['Ge',   -1.374186000,   0.991545000,   1.929067000,32],
['Bi',   -0.000097000,  -1.192952000,  -1.823965000,83],
['Sn',    0.000143000,   2.639297000,   0.112343000,50],
['Sn',    1.607674000,  -1.821066000,   0.703644000,50],
['Bi',   -2.122988000,   0.712313000,  -0.831255000,83],
['Sn',   -1.607759000,  -1.821064000,   0.703474000,50],
['Ge',    1.374437000,   0.991180000,   1.929002000,32],
['Ge',   -0.000180000,  -1.016175000,   2.811114000,32],
['Bi',    2.123023000,   0.712109000,  -0.831370000,83]]
#mio = Lector.obtenerCoordenadaGaussian("Cell2D_1_000007.out")
#mio = Lector.obtenerCoordenadaGaussian("Cell2D_1_000000.out")
mio = Lector.obtenerCoordenadaGaussian("frequencies.out")

energy= Lector.obtenerEnergiaGaussian("frequencies.out")
freq = Lector.obtenerFrecuenciaGaussian("frequencies.out")

print ("Energia es de:", energy)
print ("Frecuencia es de:", freq)

Impresora.escribirInputGaussian("Diego",2,mio)

transformarNumeroASimbolo(mio)

for i in mio:
	print i
print "ASDADDDDDDDDDDDDDDDDDDDD"
Impresora.escribirInputGaussian("Diego",2,mio)

open("Conganas.xyz","w")
#Impresora.escribirArchivoXYZ("Conganas",3,"Veamos",transformado)
#Impresora.escribirArchivoXYZ("Conganas",3,"Veamos2",transformado)

#######################################################
#print "WWWWWW",mio
plano = Genetic.createRandomPlane()
#Genetic.rotarMolecula(mio)
#print "CENTRANDO"
Genetic.centrarMolecula(mio)

#HAY QUE FORMAR ESTE HASH ANTES
hashtotal = {"Bi":3,"Sn":3,"Ge":3,"all":9}
Genetic.posicionEnPlano(plano,love)
Genetic.posicionEnPlano(plano,love2)
finalCoords= Genetic.combinarMolecula(love,love2,hashtotal)

for i in finalCoords:
	print i

#Genetic.rotarMolecula(love)
print "AHSTA ACA"
print love
#ESTO VA ACA
cordinates = np.array([[row[4],row[1], row[2], row[3]] for row in love])

#print cordinates
print "EMPIEZA cordinates"
for i in cordinates:
	print i
print "FIN DE COORDINATES"
for i in love:
		print i[0],i[1],i[2],i[3],i[4]
print "preDS"

shufleguy = Genetic.mutacionMovimientoAleatorio(love)

#Xchange = Genetic.mutacionIntercambio(cordinates)
#print "ds"
for i in shufleguy:
		#print i[0],i[1],i[2],i[3]
		print i
print "MOVIMIENTO ALEATORIO FIN "

#Xchange = Genetic.mutacionIntercambio(cordinates)
Xchange = Genetic.mutacionIntercambio(love)
for i in Xchange:
		print i[0],i[1],i[2],i[3],i[4]


# print "1"
# var.PcentAtomosMutadosMovimiento=0.1
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "2"
# var.PcentAtomosMutadosMovimiento=0.2
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "3"
# var.PcentAtomosMutadosMovimiento=0.3
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "4"
# var.PcentAtomosMutadosMovimiento=0.4
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "5"
# var.PcentAtomosMutadosMovimiento=0.5
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "6"
# var.PcentAtomosMutadosMovimiento=0.6
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "7"
# var.PcentAtomosMutadosMovimiento=0.7
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "8"
# var.PcentAtomosMutadosMovimiento=0.8
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "9"
# var.PcentAtomosMutadosMovimiento=0.9
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "preDS"
# var.PcentAtomosMutadosMovimiento=1.0
# shufleguy = Genetic.mutacionMovimientoAleatorio(love)
# print "preDS"
#Genetic.centrarMolecula(love)
#for i in love:
#		print i[0],i[1],i[2],i[3]

#print "wola"
#Genetic.centrarMolecula(love)
#for i in finalCoords:
#		print i[0],i[1],i[2],i[3]

