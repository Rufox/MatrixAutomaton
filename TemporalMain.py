
import Lector
import Impresora
import Var as var
import Genetic

def transformarNumeroASimbolo(coords):
	print (var.atomic_number[2])
	for line in coords:
		#si es numero
#		print line[0]
		line[0]=var.atomic_number[int(line[0])-1]
	return coords
		

var.init()
Lector.leerArchivoParametros()


print (list(var.Big_variable))

print (var.Big_variable["numb_conf"])

#mio = Lector.obtenerCoordenadaGaussian("Cell2D_1_000007.out")
#mio = Lector.obtenerCoordenadaGaussian("Cell2D_1_000000.out")
mio = Lector.obtenerCoordenadaGaussian("frequencies.out")

energy= Lector.obtenerEnergiaGaussian("frequencies.out")
freq = Lector.obtenerFrecuenciaGaussian("frequencies.out")
print (mio)

print ("Energia es de:", energy)
print ("Frecuencia es de:", freq)

#Impresora.escribirInputGaussian("Diego",2,mio)


transformado=transformarNumeroASimbolo(mio)
Impresora.escribirInputGaussian("Diego",2,transformado)

open("Conganas.xyz","w")
Impresora.escribirArchivoXYZ("Conganas",3,"Veamos",transformado)
Impresora.escribirArchivoXYZ("Conganas",3,"Veamos2",transformado)

#######################################################
Genetic.createRandomPlane()
Genetic.rotarMolecula(transformado)