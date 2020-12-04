import numpy as np 
import random
import itertools
import Var as var


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



def RotAndTra(lista,matriz,x_centre,y_centre,z_centre):
    # Odio esta funcion
    # Rota y traslada cada punto de los 45g (ver abajo) para formar los 360g
    new =[]
    for elemento in lista:
        new.append([elemento[0] + z_centre,elemento[1] + y_centre,elemento[2] + x_centre])
        new.append([elemento[0] + z_centre,elemento[2] + y_centre, elemento[1] + x_centre])
        new.append([elemento[0] + z_centre, -elemento[1] + y_centre,elemento[2] + x_centre])
        new.append([elemento[0] + z_centre, -elemento[2] + y_centre, elemento[1] + x_centre])
        #C7
        new.append([elemento[0] + z_centre, elemento[1] + y_centre,-elemento[2] + x_centre])
        new.append([elemento[0] + z_centre, elemento[2] + y_centre,-elemento[1] + x_centre])
        #C5
        new.append([elemento[0] + z_centre, -elemento[1] + y_centre,-elemento[2] + x_centre])
        new.append([elemento[0] + z_centre, -elemento[2] + y_centre, -elemento[1] + x_centre])
        #C4
        new.append([-elemento[0] + z_centre,elemento[1] + y_centre,elemento[2] + x_centre])
        new.append([-elemento[0] + z_centre,elemento[2] + y_centre, elemento[1] + x_centre])
        #C1
        new.append([-elemento[0] + z_centre, -elemento[1] + y_centre,elemento[2] + x_centre])
        new.append([-elemento[0] + z_centre, -elemento[2] + y_centre, elemento[1] + x_centre])
        #C3
        new.append([-elemento[0] + z_centre, elemento[1] + y_centre,-elemento[2] + x_centre])
        new.append([-elemento[0] + z_centre, elemento[2] + y_centre,-elemento[1] + x_centre])
        #C2
        new.append([-elemento[0] + z_centre, -elemento[1] + y_centre,-elemento[2] + x_centre])
        new.append([-elemento[0] + z_centre, -elemento[2] + y_centre, -elemento[1] + x_centre])
        # Cambio de eje
        if (elemento[2]!=elemento[0]):
            new.append([elemento[2] + z_centre,elemento[1] + y_centre,elemento[0] + x_centre])
            new.append([elemento[2] + z_centre,elemento[0] + y_centre, elemento[1] + x_centre] )

            new.append([elemento[2] + z_centre, -elemento[1] + y_centre,elemento[0] + x_centre] )
            new.append([elemento[2] + z_centre, -elemento[0] + y_centre, elemento[1] + x_centre] )

            new.append([elemento[2] + z_centre, elemento[1] + y_centre,-elemento[0] + x_centre])
            new.append([elemento[2] + z_centre, elemento[0] + y_centre,-elemento[1] + x_centre])

            new.append([elemento[2] + z_centre, -elemento[1] + y_centre,-elemento[0] + x_centre])
            new.append([elemento[2] + z_centre, -elemento[0] + y_centre, -elemento[1] + x_centre] )

            new.append([-elemento[2] + z_centre,elemento[1] + y_centre,elemento[0] + x_centre] )
            new.append([-elemento[2] + z_centre,elemento[0] + y_centre, elemento[1] + x_centre] )

            new.append([-elemento[2] + z_centre, -elemento[1] + y_centre,elemento[0] + x_centre] )
            new.append([-elemento[2] + z_centre, -elemento[0] + y_centre, elemento[1] + x_centre] )

            new.append([-elemento[2] + z_centre, elemento[1] + y_centre,-elemento[0] + x_centre] )
            new.append([-elemento[2] + z_centre, elemento[0] + y_centre,-elemento[1] + x_centre] )

            new.append([-elemento[2] + z_centre, -elemento[1] + y_centre,-elemento[0] + x_centre] )
            new.append([-elemento[2] + z_centre, -elemento[0] + y_centre, -elemento[1] + x_centre] )
        #####
        # Cambio eje
        if (elemento[1]!=elemento[0] and elemento[1]!=elemento[2 ]):
            new.append([elemento[1] + z_centre,elemento[0] + y_centre,elemento[2] + x_centre])
            new.append([elemento[1] + z_centre,elemento[2] + y_centre, elemento[0] + x_centre])

            new.append([elemento[1] + z_centre, -elemento[0] + y_centre,elemento[2] + x_centre])
            new.append([elemento[1] + z_centre, -elemento[2] + y_centre, elemento[0] + x_centre])
        #C7
            new.append([elemento[1] + z_centre, elemento[0] + y_centre,-elemento[2] + x_centre])
            new.append([elemento[1] + z_centre, elemento[2] + y_centre,-elemento[0] + x_centre])
        #C5
            new.append([elemento[1] + z_centre, -elemento[0] + y_centre,-elemento[2] + x_centre])
            new.append([elemento[1] + z_centre, -elemento[2] + y_centre, -elemento[0] + x_centre])

            new.append([-elemento[1] + z_centre,elemento[0] + y_centre,elemento[2] + x_centre])
            new.append([-elemento[1] + z_centre,elemento[2] + y_centre, elemento[0] + x_centre])

            new.append([-elemento[1] + z_centre, -elemento[0] + y_centre,elemento[2] + x_centre])
            new.append([-elemento[1] + z_centre, -elemento[2] + y_centre, elemento[0] + x_centre])
        #C7
            new.append([-elemento[1] + z_centre, elemento[0] + y_centre,-elemento[2] + x_centre])
            new.append([-elemento[1] + z_centre, elemento[2] + y_centre,-elemento[0] + x_centre])
        #C5
            new.append([-elemento[1] + z_centre, -elemento[0] + y_centre,-elemento[2] + x_centre])
            new.append([-elemento[1] + z_centre, -elemento[2] + y_centre, -elemento[0] + x_centre])
    # eliminacion de repetidos
    #print "WOWO",matriz.shape[2]
    tupled_lst = set(map(tuple, new))
    lst = map(list, tupled_lst)
    lista_vecinos_circulo =np.array([x for x in lst if x[0]>=0 and x[1]>=0 and x[2]>=0]) # ESTO ELIMINA LOS NEGATICOS)
    lista_vecinos_circulo =np.array([x for x in lista_vecinos_circulo if x[0]<=(matriz.shape[0]-1) and x[1]<=(matriz.shape[1]-1) and x[2]<=(matriz.shape[2]-1)]) # ESTO ELIMINA LOS muy altos)
    return (lista_vecinos_circulo).tolist()  # me gusstan mas las listas

def midPointCircleDraw(r,z,correctos): 
    # A esta funcion hau que creerle
    # Hace un perimetro de un circulo
    x = r 
    y = 0
    correctos.append([z,y,x])
    P = 1 - r  
    while (x > y) :    
        y += 1 
        # Mid-pois inside or on the  
        # perimeter  
        if (P <= 0):  
            P = P + 2 * y + 1     
        # Mid-pois outside the perimeter  
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
          
        # All the perimeter points have  
        # already been printed  
        if (x < y): 
            break
        correctos.append([z,y,x])
    return correctos

def calculateInside(coordinates):
    # Odio esta funcion.
    # revisa todo el interior de un circulo
    # se toma 0-x, 0-y, 0-(z-1) poruqe asi funciona (abra matematicas por detras, ni idea)
    bad = []
    for point in coordinates:
        for z in range(0,point[0]+1):
            for y in range(0,point[1]+1):
                for x in range(0,point[2]):
                    if(z== 0 and x==0 and y==0):
                        continue
                    else:
                        bad.append([z,y,x])
    return bad
# Driver Code 

def almacenarCoord(a,b,c):
    return a,b,c

#en esta funcion se obtiene la lista de elementos y se realiza el escalamiento de los 
#elementos en funcion de los valores de radio atomico
def obtenerElementos():
    global lista_elementos, atomos, conversion, elementos, numeros, elementos_escalados, tamanno
    
    lista_elementos=[]
    elementos=[]
    numeros=[]
    atomos=[]
    conversion=[]
    elementos_escalados = []
    tamanno=0

    with open ('Config.in', 'rt') as Config: 
        for lineas in Config:
            if 'chemical_formula' in lineas:
                chemical_formula = lineas
                input_elementos = chemical_formula.split()
                input_elementos.remove("chemical_formula")
                input_elementos.remove("=")
                for i in input_elementos:
                    #si en la linea de chemical_formula se encuentra un numero 
                    #se annade a la lista numeros, si no, a la lista elementos.
                    if i.isdigit():
                        numeros.append(i)
                    else:
                        elementos.append(i+' ')
                for j in range(len(elementos)):
                    #en lista_elementos se agregan los elementos, las veces que determinen los numeros
                    #p/e: H 2 O 1 se traduce en lista_elementos = [H, H, O]
                    lista_elementos.append(elementos[j].split()*int(numeros[j]))
                    
                    #la lista atomos es una lista de la clase Atomo, en esta lista
                    #se almacenan diferentes atributos: los elementos, su radio atomico y la escala
                    #por ahora se inicializa en 0, la escala se utiliza para el espaciado del vecindario 
                    atomos.append(Atomo(elementos[j].strip(),atomic_radii[elementos[j].strip()],0))
                    
                    elementos[j] = elementos[j].strip()
            #con el siguiente sort se ordenan los atomos en orden ascendente
            #dependiendo del radio atomico
            atomos.sort(key=lambda atomos: atomos.radio_atomico)
            #print "Estamos en la Funcion"
            #print "ATOMSO",atomos
            for l in range(len(atomos)):
                #para el l = 0, o sea para el primero atomo, el de menor radio atomico
                if l == 0:
                    #creo que esta lista conversion no sirve de mucho XD
                    conversion.append(1.0)
                    #se asigna la escala de valor 1, lo que significa que en una funcion posterior
                    #se buscaran sus vecinos directos.
                    atomos[l].escala = 1.0
                    #en esta lista se almacenan los elementos ya escalados
                    elementos_escalados.append(atomos[l].elemento)
                    #print str(atomos[l].elemento), str(atomos[l].radio_atomico), str(atomos[l].escala)
                else:
                    #para los demas atomos con radio atomicos mayores se realiza 
                    #la regla de 3 
                    tmp=float(atomos[l].radio_atomico)/float(atomos[0].radio_atomico)
                    tmp=round(int(tmp))
                    conversion.append(tmp)
                    atomos[l].escala = tmp
                    elementos_escalados.append(atomos[l].elemento)
            #   print elementos_escalados
                    #print str(atomos[l].elemento), str(atomos[l].radio_atomico), str(atomos[l].escala)
            #print "\n",conversion
            #print lista_elementos
            lista_elementos = list(itertools.chain(*lista_elementos))
            if atomos:
                break
            #print elementos, numeros, elementos_escalados, lista_elementos
    #se retorna la lista de elementos en este estilo : lista_elementos = [H, H, O]
    return lista_elementos

def buscarVecinos(m,a,b,c):
    #lista que almacena los posibles vecinos
    global posibles_vecinos
    
    #combinatoria que busca todos los vecinos posibles en 3d
    #el espaciado esta definido por el elemento actual, como se explico antes
    for i in [a,a+espaciado,a-espaciado]:
        for j in [b,b+espaciado,b-espaciado]:
            for k in [c,c+espaciado,c-espaciado]:
                #si son las mismas coordenadas del atomo; pass.
                if a == i and b == j and c == k:
                    pass
                #si es un numero negativo o supera los bordes de la matriz: pass.
                elif i < 0 or i > sum(numeros2) or j < 0 or j > sum(numeros2) or k < 0 or k > 3:
                    pass
                #si las coordenadas no estan en la lista y no estan en la franja, almacena las coordenadas en
                #la lista, y almacena eso en posibles_vecinos   
                elif almacenarCoord(i,j,k) not in lista and almacenarCoord(i,j,k) not in franja:
                    lista.append(almacenarCoord(i,j,k))
                    posibles_vecinos = lista
                    #print (i,j,k)
    #se retorna la lista con los posibles vecinos del atomo actual
    return posibles_vecinos

# lo mismo que la anterior pero solo con vecinos directos
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

#esta funcion era para guardar la informacion en el output .xyz
def guardar(fr):
    global grupo_atomico

    f=open ('hola.xyz','a')
    f.write(str(grupo_atomico.n) +'\nMatrix\n')
    for i in range(len(fr)):
        f.write(str(matriz[fr[i][2],fr[i][1],fr[i][0]])+' '+str(fr[i][0])+' '+str(fr[i][1])+' '+str(fr[i][2])+'\n')
    f.close()

def obtenerCoordenadas(fr):
    arreglo = np.array(fr)
    arreglo = arreglo*float(atomos[0].radio_atomico)*2*var.PCentCloseness
    for i in range(len(fr)):
        coords_list.append(str(matriz[fr[i][0],fr[i][1],fr[i][2]])+' '+str(round(arreglo[i][0],2))+' '+str(round(arreglo[i][1],2))+' '+str(round(arreglo[i][2],2)))
    coords_list2.append(coords_list)
    return coords_list2

#def main():
def Llamar(iteraciones, tipo):
#   iteraciones =2
    global x, y, z, matriz, franja, coords_list, coords_list2
    global grupo_atomico
    global atomic_radii
    global numeros2
    global lista
    global espaciado # Radio
    global tamanno
    
    coords_list = []
    coords_list2 = []   # Lista de Listas, final q se entrega
    lista = []
    franja = [] # Lista con coordenadass finales de cada iteracion
    franja_error = [] # Franja con las posiciones incorrectas

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

    lista_elementos = obtenerElementos()
    #se invierte el orden de los elementos para trabajar desde el primero
    #(deberia haber trabajado con colas para no hacer esta estupidez pero bue)
    #lista_elementos.reverse()
    # Diego: se toman como aleatorio el orden de los elementos
    if(var.shuffleElements == 1):
        np.random.shuffle(lista_elementos)
    #print "Imprimineto lista_elementos"
    print("Orden de adicion: ",lista_elementos)
    #exit(1)
    #esta es una conversion de la lista numeros en enteros, porque estaban como string
    numeros2 = map(int, numeros)
    #print "Imprimiento lista numeros2"
    #print numeros2
    #print "TAMAnnO, ",tamanno
    #print atomos
    #print numeros
    #print elementos
    maxim = 0
    for el in range(len(atomos)):
        tmp=int(atomos[el].escala) * int(numeros[el])
        #print tmp ,  atomos[el].escala, numeros[el]
        if atomos[el].escala >maxim:
            maxim=int(atomos[el].escala)
        tamanno+=tmp
    #maximo = max(atomos)
    #print maxim
    #exit(1)
    #print tamanno
    #exit(1)
    #se define el grupo atomico con la clase GrupoAtomico(n), el n esta definido por la
    #suma de los elementos de la lista numeros.
    grupo_atomico = GrupoAtomico(tamanno)
    #print grupo_atomico
    #esto lo hice para poder trabajar con los elementos y no afectar a la lista_elementos
    #atomos_ga = [grupo_atomico.atomos.insert(0,x) for x in lista_elementos]
    #print "ACA", grupo_atomico

    while iteraciones > 0:
        np.random.shuffle(lista_elementos)
        print("EMPIEZA CICLO\n")
        posibles_vecinos_completos=[]
        #Se guardan los elementos en lista_elementos, el funcionamiento de 
        #obtenerElementos() mejor detallado en la funcion
        #creacion de la matriz 
        #matriz = np.zeros((grupo_atomico.n+1)**3, dtype = object).reshape(grupo_atomico.n+1,grupo_atomico.n+1,grupo_atomico.n+1)        # 3d array
        #print matriz
        #eleccion de posicion random para primer elemento
        indices =  np.random.randint(0, high=grupo_atomico.n+1, size=3)
        print(atomos[0])
        print("Tamanno de la wea es:",grupo_atomico.n +1)
        if(tipo ==1):
            matriz = np.zeros((grupo_atomico.n+maxim), dtype = object).reshape(1,1,grupo_atomico.n+maxim)
            y = 0
            z = 0
        elif (tipo == 2):
            matriz = np.zeros((grupo_atomico.n+maxim)**2, dtype = object).reshape(1,grupo_atomico.n+maxim,grupo_atomico.n+maxim)        # 3d array
            y=indices[1]
            z = 0
        else:
            matriz = np.zeros((grupo_atomico.n+maxim)**3, dtype = object).reshape(grupo_atomico.n+maxim,grupo_atomico.n+maxim,grupo_atomico.n+maxim)        # 3d array          
            y=indices[1]
            z=indices[2]
        #print indices
        x=indices[0]
#       print "Coordenadas generadas para primer atomo ( x:",x,", y:",y,", z:",z,")"

        #la franja almacena las coordenadas de todos los atomos del gurpo atomico por iteracion
        #por ahora se almacenan las coordenadas del primer atomo
        franja.append(almacenarCoord(z,y,x))
        
        # en las coordenadas elegidas para el primer atomo se ubica el primer elemento de la lista_elementos
        matriz[(z,y,x)] = lista_elementos[-1]#.pop()
#       print "Se agrego el atomo: ",lista_elementos[-1]

        # Esta lista indica todas las posiciones PROHIBIDAS de las posibles
        Malos_total=[[z,y,x]]#np.array([x,y,z])
        #print Malos_total
#       Malos_total.append([x,y,z])
        #Se buscan los vecinos del primer atomo
        #detalles en la funcion v
        ##buscarVecinos(matriz,x,y,z)
        #exit(1)
        for i in atomos:
            if matriz[z,y,x] == i.elemento:
                #           #se determina el espaciado dependiendo de la escala del elemento actual
                espaciado = int(i.escala)
                break
        #print "Escalas:",i,int(i.escala) 

        #while len(franja) < grupo_atomico.n:
        # varibla contadora, vital
        aux = 0
        while aux<len(lista_elementos)-1:
            print("\nCoordenadas en sistema (z,y,x): ",franja)
            print("Se agrego el atomo (pasado): ",lista_elementos[-aux-1])
            print("Radio trabajado corresponde: ",espaciado)
            # CorrectosX es una lista con las posiciones de posibles
            # vecinos de medio cuadrante de circulo (45g), plano XY, perimetro
            correctosX = []
            # posicoines incorrectas del mismo plano anterior, interior circulo
            bad = []
            Z = 0
            # funcion que construye circulo, pide radio, valor de Z (0 ahora) y array a guardar
            midPointCircleDraw(espaciado, Z, correctosX) 
            franjaX = np.asarray(correctosX)
            for cara_1 in franjaX:
                if(cara_1[1] ==0):
                    pass
                else:
                    Z+=1
                    midPointCircleDraw(cara_1[2],Z,correctosX)
            if(espaciado!=1):
                bad =calculateInside(correctosX)
                tupled_lst = set(map(tuple, bad))
                lst_bad = map(list, tupled_lst)
                Malos_total.extend(RotAndTra(lst_bad,matriz,franja[aux][2],franja[aux][1],franja[aux][0]))
            
            # Aca CorrectosX tiene el perimetro 45g de el plano XY, XY Z=1, XY Z=2.... XY Z=X
            #print 'Posibles vecinos: (No centrados)', correctosX


            posibles_vecinos = RotAndTra(correctosX,matriz,franja[aux][2],franja[aux][1],franja[aux][0])
            # En este punto posibles_vecinos tiene TODO la superficie de una esfera radio "espaciado"
            #print "Final Posibles Ubicaciones:",posibles_vecinos
            # A todos las buenas posiciones, se eliminan las malas posiciones
            posibles_vecinos_completos.extend(posibles_vecinos)
            #print "Final Posibles Ubicaciones RECUERDA:",posibles_vecinos_completos
            #print "MALOS TOTAL: ",Malos_total
            posibles_vecinos_completos = [i for i in posibles_vecinos_completos if i not in Malos_total[:]] 
            #DIBUJO
            #for data in posibles_vecinos:
            #   matriz[data[0],data[1],data[2]]=2
            #print matriz
            #DINUJO
            
            #se elige aleatoriamente un posible vecino y se asigna a la variable vecino_candidato
            #print "Final Posibles Ubicaciones RECUERDA - MALOS:",posibles_vecinos_completos
            vecino_candidato = random.choice(posibles_vecinos_completos)
            Malos_total.extend([vecino_candidato])
            
            franja.append(almacenarCoord(vecino_candidato[0],vecino_candidato[1],vecino_candidato[2]))
            print("Atomo a ingresar: ", lista_elementos[-aux-2], "en (z,y,x): ", vecino_candidato)
            matriz[(vecino_candidato[0],vecino_candidato[1],vecino_candidato[2])]=lista_elementos[-aux-2]#.pop()
            #print matriz
            #exit(2)    
            for i in atomos:
                if matriz[(vecino_candidato[0],vecino_candidato[1],vecino_candidato[2])] == i.elemento:
            #           #se determina el espaciado dependiendo de la escala del elemento actual
                    espaciado=int(i.escala)   #ESCALALAALAL
            #       else:
            #           continue
            
            #   if espaciado > 1:
            #       # si el espaciado es mayor a 1 se verifica si existen vecinos directos
            #       while existenVecinosDirectos(matriz,vecino_candidato[0],vecino_candidato[1],vecino_candidato[2]):
            #           #de existir vecinos directos, se hace una especie de backtracking 8-)
            #           #se vuelve a agregar el elemento que se ubico en la matriz a la lista_elementos
            #           lista_elementos.append(matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])])
            #           #se le vuelve a asignar un 0 a esa coordenada, en vez del elemento
            #           matriz[(vecino_candidato[2],vecino_candidato[1],vecino_candidato[0])] = 0
            #           #se elimina este candidato de los posibles vecinos para no poder seleccionarlo mas
            #           posibles_vecinos.remove((vecino_candidato[0],vecino_candidato[1],vecino_candidato[2]))
            #           #print vecino_candidato, posibles_vecinos
                        
            #           #se escoge otro candidato de la lista posibles_vecinos y ahora el nuevo_candidato es el vecino_candidato
            #           nuevo_candidato = random.choice(posibles_vecinos)
            #           vecino_candidato = nuevo_candidato
            #           #print lista_elementos
            #       #si no existen vecinos directos del vecino_candidato, se convierte en el vecino_escogido
            #       else:
            #           #print existenVecinosDirectos(matriz, vecino_candidato[0],vecino_candidato[1],vecino_candidato[2])
            #           vecino_escogido = vecino_candidato
            #           #se agrega el vecino_escogido a la franja de solucion para la iteracion actual
            #           franja.append(vecino_escogido)
            #           #print espaciado
            #           #print 'Vecino escogido: ',(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
                        

            #           #Se buscan los posibles vecinos del vecino_escogido actual
            #           buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
            #           #print 'Posibles vecinos: ', posibles_vecinos
            #           #print matriz
            #   #si el espaciado es 1, no importa si existen vecinos directos:
            #   else:
            #       #el vecino_escogido es el vecino candidato y se annaden las coordenadas a la franja
            #       vecino_escogido = vecino_candidato
            #       franja.append(vecino_escogido)
            #       #print espaciado
            #       #print 'Vecino escogido: ',(vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
                    
            #       #Se buscan los vecinos para el vecino_escogido
            #       buscarVecinos(matriz,vecino_escogido[0],vecino_escogido[1],vecino_escogido[2])
            #       #print 'Posibles vecinos: ', posibles_vecinos
            aux+=1
            #print "aux:",aux
            #print "\n"
        #print "UBICACIONES:",franja
        iteraciones = iteraciones - 1
        #guardar(franja)
        
        #funcion para obtener una lista de las franjas de solucion por la cantidad de iteraciones determianda
        obtenerCoordenadas(franja)
        #for data in Malos_total:
        #   matriz[data[0],data[1],data[2]]=0
        #for data in posibles_vecinos_completos:
        #   matriz[data[0],data[1],data[2]]=2
        #for data in franja:
        #   matriz[data[0],data[1],data[2]]="T"
        #se reinician estas listas para la nueva iteracion
        franja = [] 
        coords_list = []
        #exit(1)
    #print Malos_total
    #print coords_list2
    return coords_list2
    #MatrixAutomaton.obtenerCoordenadas(franja)
        


if __name__=="__main__":
    main();