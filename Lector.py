import configparser
import Var as var

#Este programa en particular sera el encargado de extraer (leer) cualquier informacion de algun archivo de texto.

# Leer archivo de configuracion "Config.in" y guarda todas sus variables
# Archivo de configuracon DEBE ir con [SECCIONES]

# Falta:
# nombre de archivo de configuracion entregado por terminal
# verificacion que todas las variables de dicho archivo de configuracon existan en realidad
# verificacioes que todas los datos de cada variable corresponda a algo real.

def leerArchivoParametros(configs):
	config = configparser.ConfigParser()

	config.read(configs)

	for secciones in config.sections():
		for (variable, valor) in config.items(secciones):
			agregarVariableGlobal(variable, valor)
	var.establecerVariablesDefault()

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
		    words = int(line.split()[1]),round(float(line.split()[3]),4),round(float(line.split()[4]),4),round(float(line.split()[5]),4)
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
def obtenerTermination(file):
	print "llamasdo a",file
	try:
		archivo = open(file,"r")
		rline = archivo.readlines()
		correcto = 1
		for i in range(len(rline)):
			if "combination of multiplicity impossible" in rline[i]:
				print "ERROR DE COMBINACION DE MULTIPLLICIDAD"
				exit(1)
			if "Small interatomic distances encountered:" in rline[i]:
				correcto = 3
				break
			elif "Error termination" in rline[i]:
				correcto = 2
				break
			elif "Normal termination" in rline[i]:
				correcto = 0
				break
		return correcto
	except (OSError, IOError):
		return 1
	#return archivo.read().splitlines()[-1]
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

def leerLOGS():
	#energia, ciclo, pre o post, 
	ciclo = 0
	energia = 1
	converg = 1
	name = ""

	archivo = open("LOGS","r")
	rline = archivo.readlines()
	for i in range(len(rline)):
		if ( "Ciclo" in rline[i]):
			ciclo = int(rline[i].split("=")[-1])
		if ("Energia" in rline[i]):
			energia = float((rline[i].split(":")[-1]).split()[0])
		if ("Convergencia" in rline[i]):
			converg = float(rline[i].split()[1])
		#if ("Convergencia" in rline[i]):
		#	converg = int(rline[i].split()[-1])
	print ciclo, converg, energia
	#VERIFICA QUE PRECOORDS ciclo+1 existe. SI no funcionara con POSTCORDS ciclo
	#if
	toRead=""
	existe = True
	try:
		f = open("PostCoords_"+str(ciclo)+".xyz")
		f.close()
	except (OSError, IOError):
		existe = False
	if existe == True:
		toRead= "PostCoords_"+str(ciclo)+".xyz"
	else:
		toRead= "PostCoords_"+str(ciclo-1)+".xyz"
	return ciclo,converg,energia,toRead

def leerInformacionXYZ(file):
	print "Leyendo ",file
	archivo = open(file,"r")
	rline = archivo.readlines()
	atom = int(rline[0])
	energy = []
	coords = []

	aux = 1
	tmp_c=[]
	coords = []
	for i in range(1,len(rline)):
		#print rline[i]
		if (aux == 1): # ESTAMOS EN LOS NOMBRES Y ENERGIA
			tmp = float(rline[i].split()[-2])
			#print tmp
			energy.append(tmp)
		elif aux==0:
			#print rline[i]
			pass
		else:
#			words = int(line.split()[1]),
#					round(float(line.split()[3]),4),
#					round(float(line.split()[4]),4),
#					round(float(line.split()[5]),4)
			tmp = rline[i].split()
			na = int(var.atomic_number.index(tmp[0])+1)
			words = tmp[0],float(tmp[1]),float(tmp[2]),float(tmp[3]),na
			L = list(words)
			coords.append(L)
			#print words
			#print na
		aux+=1
		if (aux==(atom+2)):
			#print "LINEA siguiente ",rline[i+1]
			tmp_c.append(coords)
			coords = []
			aux=0
			#exit(1)
	#print tmp_c
	#print energy
	archivo.close()
	return energy, tmp_c