import configparser
import Var as var

#Este programa en particular sera el encargado de extraer (leer) cualquier informaicon de algun archivo de texto.

# Leer archivo de configuracion "Config.in" y guarda todas sus variables
# Archivo de configuracon DEBE ir con [SECCIONES]

# Falta:
# nombre de archivo de configuracion entregado por terminal
# verificacion que todas las variables de dicho archivo de configuracon existan en realidad
# verificacioes que todas los datos de cada variable corresponda a algo real.
def leerArchivoParametros():
	config = configparser.ConfigParser()

	config.read('Config.in')

	for secciones in config.sections():
		for (variable, valor) in config.items(secciones):
			#print variable, valor
			agregarVariableGlobal(variable, valor)

def agregarVariableGlobal(key, dato):
	var.Big_variable[key]=dato

# Busca inforamcion coordenadas de archivo gaussian de salida. En caso de error retorna 0
def obtenerCoordenadaGaussian(file):
	start=0
	try:
		archivo = open(file,"r")
		rline = archivo.readlines()
		for i in range (len(rline)):
		    if "Standard orientation:" in rline[i]:
		        start = i

		for m in range (start + 5, len(rline)):
		    if "---" in rline[m]:
		        end = m
		        break
		if start==0:
			return 0

		coords=[]
		for line in rline[start+5 : end] :
		    words = int(line.split()[1]),float(line.split()[3]),float(line.split()[4]),float(line.split()[5])
		    L=list(words)
		    coords.append(L)
		return coords
	except (OSError, IOError):
		print "Archivo no encontrado --> ",file
		exit(1)


# Busca inforamcion energetica de archivo gaussian de salida. En caso de error retorna 0
def obtenerEnergiaGaussian(file):
	energy=0
	archivo = open(file,"r")
	rline = archivo.readlines()
	for i in range (len(rline)):
	    if "SCF Done:" in rline[i]:
	        energy = rline[i].split()[4]
	return energy

# EL programa original toma las coordenadas de la frecuencias y le SUMA dicha correccion
# a las coordenadas originales
def obtenerFrecuenciaGaussian(file):
	freq=0
	archivo = open(file,"r")
	rline = archivo.readlines()
	for i in range (len(rline)):
	    if "Zero-point correction" in rline[i]:
	        freq = rline[i].split()[2]
	return freq