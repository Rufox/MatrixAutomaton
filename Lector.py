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

def obtenerCoordenadaGaussian(file):
	start=0
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
	    words = line.split()[1],line.split()[3],line.split()[4],line.split()[5]
	    coords.append(words)
	
	#print "TOTAL: ", coords
	#print "Primero ", 		coords[0]
	#print "Y segundo ", 		coords[1][2]
	return coords

#def obtenerEnergiaGaussian():
#def obtenerFrecuenciaGaussian():
