import numpy as np 
import random
import itertools

class GrupoAtomico:
	def __init__(self, n):
		self.atomos = []
		self.n = n

	def __str__(self):
		return "N: {}, Atomos: {}\n".format(self.n, self.atomos)

	def __repr__(self):
		return str(self)

class Atomo:
    def __init__(self, elemento, radio_atomico, escala):
        self.elemento = elemento
        self.radio_atomico = radio_atomico
        self.escala = escala

    def __str__(self):
    	return "Elemento: {}, Atomic Radii: {}, Escala: {}\n".format(self.elemento, self.radio_atomico, self.escala)
        #return str(self.elemento)+ "dd"+ str(self.radio_atomico)
    def __repr__(self):
    	return str(self)

def almacenarCoord(a,b,c):
	return a,b,c

def obtenerElementos():
	global lista_elementos, atomos, conversion, elementos, numeros, elementos_escalados
	lista_elementos=[]
	elementos=[]
	numeros=[]
	atomos=[]
	conversion=[]
	elementos_escalados = []

	with open ('Config.in', 'rt') as Config: 
	    for lineas in Config:
	    	if 'chemical_formula' in lineas:
	    		chemical_formula = lineas
	    		input_elementos = chemical_formula.split()
	    		input_elementos.remove("chemical_formula")
	    		input_elementos.remove("=")
	    		for i in input_elementos:
	    			if i.isdigit():
	    				numeros.append(i)
	    			else:
	    				elementos.append(i+' ')
	    		for j in range(len(elementos)):
					lista_elementos.append(elementos[j].split()*int(numeros[j]))
					atomos.append(Atomo(elementos[j].strip(),atomic_radii[elementos[j].strip()],0))
					elementos[j] = elementos[j].strip()
			atomos.sort(key=lambda atomos: atomos.radio_atomico)

			for l in range(len(atomos)):
				if l == 0:
					conversion.append(1.0)
					atomos[l].escala = 1.0
					elementos_escalados.append(atomos[l].elemento)
					#print str(atomos[l].elemento), str(atomos[l].radio_atomico), str(atomos[l].escala)
				else:
					tmp=float(atomos[l].radio_atomico)/float(atomos[0].radio_atomico)
					tmp=round(int(tmp))
					conversion.append(tmp)
					atomos[l].escala = tmp
					elementos_escalados.append(atomos[l].elemento)
					#print str(atomos[l].elemento), str(atomos[l].radio_atomico), str(atomos[l].escala)
			print conversion
			lista_elementos = list(itertools.chain(*lista_elementos))
			#print elementos, numeros, elementos_escalados, lista_elementos

	return lista_elementos

def buscarVecinos(m,a,b,c):
	global posibles_vecinos
	
	for i in [a,a+espaciado,a-espaciado]:
		for j in [b,b+espaciado,b-espaciado]:
			for k in [c,c+espaciado,c-espaciado]:
				if a == i and b == j and c == k:
					pass
				elif i < 0 or i > sum(numeros2) or j < 0 or j > sum(numeros2) or k < 0 or k > 3:
					pass
				elif almacenarCoord(i,j,k) not in lista and almacenarCoord(i,j,k) not in franja:
					lista.append(almacenarCoord(i,j,k))
					posibles_vecinos = lista
					#print (i,j,k)
	return posibles_vecinos

def existenVecinosDirectos(m,a,b,c):
	new =[]
	
	for i in [a,a+1,a-1]:
		for j in [b,b+1,b-1]:
			for k in [c,c+1,c-1]:
				if a == i and b == j and c == k:
					pass
				elif i < 0 or i > sum(numeros2) or j < 0 or j > sum(numeros2) or k < 0 or k > 3:
					pass
				elif almacenarCoord(i,j,k) not in new and almacenarCoord(i,j,k) not in franja:
					#print (i,j,k), matriz[(k,j,i)]
					if matriz[(k,j,i)] != 0:
						return True
	return False

def guardar(fr):
	global grupo_atomico

	f=open ('hola.xyz','a')
	f.write(str(grupo_atomico.n) +'\nMatrix\n')
	for i in range(len(fr)):
		f.write(str(matriz[fr[i][2],fr[i][1],fr[i][0]])+' '+str(fr[i][0])+' '+str(fr[i][1])+' '+str(fr[i][2])+'\n')
	f.close()

def obtenerCoordenadas(fr):
	arreglo = np.array(fr)
	arreglo = arreglo*float(atomos[0].radio_atomico)
	for i in range(len(fr)):
		coords_list.append(str(matriz[fr[i][2],fr[i][1],fr[i][0]])+' '+str(round(arreglo[i][0],2))+' '+str(round(arreglo[i][1],2))+' '+str(round(arreglo[i][2],2)))
	coords_list2.append(coords_list)
	return coords_list2

def main():
	global x, y, z, matriz, franja, coords_list, coords_list2
	global iteraciones, grupo_atomico
	global atomic_radii
	global numeros2
	global lista
	global espaciado
	
	coords_list = []
	coords_list2 = []
	lista = []
	franja = []	

	atomic_radii = {'H':'0.31', 'He':'0.28', 'Li':'1.28', 'Be':'0.96',
                    'B' :'0.84', 'C' :'0.76', 'N' :'0.71', 'O' :'0.66',
                    'F' :'0.57', 'Ne':'0.58', 'Na':'1.66', 'Mg':'1.41',
                    'Al':'1.21', 'Si':'1.11', 'P' :'1.07', 'S' :'1.05',
                    'Cl':'1.02', 'Ar':'1.06', 'K' :'2.03', 'Ca':'1.77',
                    'Sc':'1.70', 'Ti':'1.60', 'V' :'1.53', 'Cr':'1.39',
                    'Mn':'1.39', 'Fe':'1.32', 'Co':'1.26', 'Ni':'1.24',
                    'Cu':'1.32', 'Zn':'1.22', 'Ga':'1.22', 'Ge':'1.20',
                    'As':'1.19', 'Se':'1.20', 'Br':'1.20', 'Kr':'1.16',
                    'Rb':'2.20', 'Sr':'1.95', 'Y' :'1.90', 'Zr':'1.75',
                    'Nb':'1.64', 'Mo':'1.54', 'Tc':'1.47', 'Ru':'1.46',
                    'Rh':'1.42', 'Pd':'1.39', 'Ag':'1.45', 'Cd':'1.44',
                    'In':'1.42', 'Sn':'1.39', 'Sb':'1.39', 'Te':'1.38',
                    'I' :'1.39', 'Xe':'1.40', 'Cs':'2.44', 'Ba':'2.16',
                    'La':'2.07', 'Ce':'2.04', 'Pr':'2.03', 'Nd':'2.01',
                    'Pm':'1.99', 'Sm':'1.98', 'Eu':'1.98', 'Gd':'1.96',
                    'Tb':'1.94', 'Dy':'1.92', 'Ho':'1.92', 'Er':'1.89',
                    'Tm':'1.90', 'Yb':'1.87', 'Lu':'1.87', 'Hf':'1.75',
                    'Ta':'1.70', 'W' :'1.62', 'Re':'1.51', 'Os':'1.44',
                    'Ir':'1.41', 'Pt':'1.36', 'Au':'1.36', 'Hg':'1.32',
                    'Tl':'1.45', 'Pb':'1.46', 'Bi':'1.48', 'Po':'1.40',
                    'At':'1.50', 'Rn':'1.50', 'Fr':'2.60', 'Ra':'2.21',
                    'Ac':'2.15', 'Th':'2.06', 'Pa':'2.00', 'U' :'1.96',
                    'Np':'1.90', 'Pu':'1.87', 'Am':'1.80', 'Cm':'1.69'}

	atomic_mass = { 'H'  :'1.0079'  ,'He':'4.003'   ,'Li' :'6.941'   ,'Be' :'9.0122',
                    'B'  :'10.811'  ,'C' :'12.018'  ,'N'  :'14.0067' ,'O'  :'15.9994', 
                    'F'  :'18.998'  ,'Ne':'20.179'  ,'Na' :'22.9897' ,'Mg' :'24.305',
                    'Al' :'26.981'  ,'Si':'28.085'  ,'P'  :'30.9738' ,'Cl' :'35.453',
                    'K'  :'39.098'  ,'Ar':'39.948'  ,'Ca' :'40.078'  ,'Sc' :'44.9559',
                    'Ti' :'47.867'  ,'V' :'50.942'  ,'Cr' :'51.9961' ,'Mn' :'54.938',
                    'Fe' :'55.845'  ,'Ni':'58.693'  ,'Co' :'58.9332' ,'Cu' :'63.546',
                    'Zn' :'65.390'  ,'Ga':'69.723'  ,'Ge' :'72.64'   ,'As' :'74.9216', 
                    'Se' :'78.960'  ,'Br':'79.904'  ,'Kr' :'83.8'    ,'Rb' :'85.4678', 
                    'Sr' :'87.620'  ,'Y' :'88.906'  , 'Zr':'91.224'  ,'Nb' :'92.9064',
                    'Mo' :'95.940'  ,'Tc':'98.000'  ,'Ru' :'101.07'  ,'Rh' :'102.9055',
                    'Pd' :'106.420' ,'Ag':'107.868' , 'Cd':'112.411' ,'In' :'114.818',
                    'Sn' :'118.710' ,'Sb':'121.760' ,'I'  :'126.9045','Te' :'127.6',
                    'Xe' :'131.290' ,'Cs':'132.906' ,'Ba' :'137.327' ,'La' :'138.9055',
                    'Ce' :'140.116' ,'Pr':'140.908' ,'Nd' :'144.24'  ,'Pm' :'145',
                    'Sm' :'150.360' ,'Eu':'151.964' ,'Gd' :'157.25'  ,'Tb' :'158.9253' ,
                    'Dy' :'162.500' ,'Ho':'164.930' , 'Er':'167.259' ,'Tm' :'168.9342',
                    'Yb' :'173.040' ,'Lu':'174.967' ,'Hf' :'178.49'  ,'Ta' :'180.9479',
                    'W'  :'183.840' ,'Re':'186.207' ,'Os' :'190.23'  ,'Ir' :'192.217',
                    'Pt' :'195.078' ,'Au':'196.967' ,'Hg' :'200.59'  ,'Tl' :'204.3833',
                    'Pb' :'207.200' ,'Bi':'208.980' ,'Po' :'209'     ,'At' :'210',
                    'Rn' :'222.000' ,'Fr':'223.000' ,'Ra' :'226'     ,'Ac' :'227',
                    'Pa' :'231.035' ,'Th':'232.038' ,'Np' :'237'     ,'U'  :'238.0289',
                    'Am' :'243.000' ,'Pu':'244'     ,'Cm' :'247'     ,'Bk' :'247', 
                    'Cf' :'251.000' ,'Es':'252'     ,'Fm' :'257'     ,'Md' :'258',
                    'No' :'259.000' ,'Rf':'261'     ,'Lr' :'262'     ,'Db' :'262',
                    'Bh' :'264.000' ,'Sg':'266'     ,'Mt' :'268'     ,'Hs' :'277'}

	f=open('hola.xyz','w+')
	iteraciones = 5
	
	while iteraciones > 0:

		lista_elementos = obtenerElementos()
		lista_elementos.reverse()
		numeros2 = map(int, numeros)
		grupo_atomico = GrupoAtomico(sum(numeros2))
		atomos_ga = [grupo_atomico.atomos.insert(0,x) for x in lista_elementos]
		print grupo_atomico
		matriz = np.zeros((grupo_atomico.n+1)**2*4, dtype = object).reshape(4,grupo_atomico.n+1,grupo_atomico.n+1)        # 3d array
		
		#eleccion de posicion random para primer elemento
		indices =  np.random.randint(0, high=3, size=3)
		x=indices[0]
		y=indices[1]
		z=random.randint(0,3)

		print "Coordenadas generadas para primer atomo ( x:",x,", y:",y,", z:",z,")"

		franja.append(almacenarCoord(x,y,z))
		
		matriz[(z,y,x)] = lista_elementos.pop()
		
		espaciado = 1
		buscarVecinos(matriz,x,y,z)
	 	#print 'Posibles vecinos: ', posibles_vecinos
	 	#print matriz

		while len(franja) < grupo_atomico.n:

			while len(lista_elementos):
				#print posibles_vecinos
				vecino_candidato = random.choice(posibles_vecinos)
				if vecino_candidato in franja:
					pass
				else:
					#print vecino_candidato
					matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])]=lista_elementos.pop()
					
					for i in atomos:
						if matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])] == i.elemento:
							espaciado=int(i.escala)
						else:
							continue
					
					if espaciado > 1:
						while existenVecinosDirectos(matriz,vecino_candidato[0],vecino_candidato[1],vecino_candidato[2]):
							
							lista_elementos.append(matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])])
							matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])] = 0
							posibles_vecinos.remove((vecino_candidato[0],vecino_candidato[1],vecino_candidato[2]))
							#print vecino_candidato, posibles_vecinos
							nuevo_candidato = random.choice(posibles_vecinos)
							vecino_candidato = nuevo_candidato
							#print lista_elementos
							
						else:
							#print existenVecinosDirectos(matriz, vecino_candidato[0],vecino_candidato[1],vecino_candidato[2])
							vecino_escogido = vecino_candidato
							franja.append(vecino_escogido)
							#print espaciado
							#print 'Vecino escogido: ',(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
							buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
							#print 'Posibles vecinos: ', posibles_vecinos
							#print matriz
					else:
						vecino_escogido = vecino_candidato
						franja.append(vecino_escogido)
						#print espaciado
						#print 'Vecino escogido: ',(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
						buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
						#print 'Posibles vecinos: ', posibles_vecinos
		print matriz
		print franja
		iteraciones = iteraciones - 1
		#guardar(franja)
		
		obtenerCoordenadas(franja)

		franja = []	
		coords_list = []
	
	print coords_list2
	#MatrixAutomaton.obtenerCoordenadas(franja)
		


if __name__=="__main__":
    main();