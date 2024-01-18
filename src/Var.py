#!/usr/bin/python
import math

GaussianCall = "Gaussian16"
extension = "log"
treshold = 3
# Diccionarios, no cambiar
software_extensions = {"orca":"inp", "gaussian":"com"}
software_extensions_output = {"orca":"out", "gaussian":extension}
atomic_number = [ "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt" ];
elementsWeight = [ 1.0079, 4.0026, 6.941, 9.0122, 10.811, 12.0107, 14.0067, 15.9994, 18.9984, 20.1797, 22.9897, 24.305, 26.9815, 28.0855, 30.9738, 32.065, 35.453, 39.948, 39.0983, 40.078, 44.9559, 47.867, 50.9415, 51.9961, 54.938, 55.845, 58.9332, 58.6934, 63.546, 65.39, 69.723, 72.64, 74.9216, 78.96, 79.904, 83.8, 85.4678, 87.62, 88.9059, 91.224, 92.9064, 95.94, 98, 101.07, 102.9055, 106.42, 107.8682, 112.411, 114.818, 118.71, 121.76, 127.6, 126.9045, 131.293, 132.9055, 137.327, 138.9055, 140.116, 140.9077, 144.24, 145, 150.36, 151.964, 157.25, 158.9253, 162.5, 164.9303, 167.259, 168.9342, 173.04, 174.967, 178.49, 180.9479, 183.84, 186.207, 190.23, 192.217, 195.078, 196.9665, 200.59, 204.3833, 207.2, 208.9804, 209, 210, 222, 223, 226, 227, 232.0381, 231.0359, 238.0289, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 262, 261, 262, 266, 264, 277, 268 ];
atomic_radii = {'H':0.31, 'He':0.28, 'Li':1.28, 'Be':0.96,
                'B' :0.84, 'C' :0.76, 'N' :0.71, 'O' :0.66,
                'F' :0.57, 'Ne':0.58, 'Na':1.66, 'Mg':1.41,
                'Al':1.21, 'Si':1.11, 'P' :1.07, 'S' :1.05,
                'Cl':1.02, 'Ar':1.06, 'K' :2.03, 'Ca':1.77,
                'Sc':1.70, 'Ti':1.60, 'V' :1.53, 'Cr':1.39,
                'Mn':1.39, 'Fe':1.32, 'Co':1.26, 'Ni':1.24,
                'Cu':1.32, 'Zn':1.22, 'Ga':1.22, 'Ge':1.20,
                'As':1.19, 'Se':1.20, 'Br':1.20, 'Kr':1.16,
                'Rb':2.20, 'Sr':1.95, 'Y' :1.90, 'Zr':1.75,
                'Nb':1.64, 'Mo':1.54, 'Tc':1.47, 'Ru':1.46,
                'Rh':1.42, 'Pd':1.39, 'Ag':1.45, 'Cd':1.44,
                'In':1.42, 'Sn':1.39, 'Sb':1.39, 'Te':1.38,
                'I' :1.39, 'Xe':1.40, 'Cs':2.44, 'Ba':2.16,
                'La':2.07, 'Ce':2.04, 'Pr':2.03, 'Nd':2.01,
                'Pm':1.99, 'Sm':1.98, 'Eu':1.98, 'Gd':1.96,
                'Tb':1.94, 'Dy':1.92, 'Ho':1.92, 'Er':1.89,
                'Tm':1.90, 'Yb':1.87, 'Lu':1.87, 'Hf':1.75,
                'Ta':1.70, 'W' :1.62, 'Re':1.51, 'Os':1.44,
                'Ir':1.41, 'Pt':1.36, 'Au':1.36, 'Hg':1.32,
                'Tl':1.45, 'Pb':1.46, 'Bi':1.48, 'Po':1.40,
                'At':1.50, 'Rn':1.50, 'Fr':2.60, 'Ra':2.21,
                'Ac':2.15, 'Th':2.06, 'Pa':2.00, 'U' :1.96,
                'Np':1.90, 'Pu':1.87, 'Am':1.80, 'Cm':1.69}

# Funciones de programa NO BORRAR NI EDITAR
def init():
    global Big_variable
    # % de mutacion para la creacion de nuecos individuos desde 0 con matrix automaton en los formatos 1D y 2D. El formato 3D nace del sobrante para el 100%
    # Valor entre 0 y 1
    global Pcent1D, Pcent2D
    #Porcentaje de atomos que sufriran unmovimiento aleatorio como mutacion.
    #Valores entre 0 y 1
    global PcentAtomosMutadosMovimiento
    # % de N a mutar (patada e intercambio)
    global PcentToMutate
    # % de N a crear en 1D, 2D, 3D (% x cada uno)
    global PcentToCreate
    # % de cercania de los atomos (default = 1), si es mayor los atomos se alejaran, menor y se acercaran.
    global PCentCloseness
    #Fitness
    # Valos alpha, no tengo idea que significa, copiado textual del programa anterior
    # FOrmula mejor = exp ^ (-alphaNumber * prob); donde prob = (Ei-Emin) / (Emax -Emin) donde Emin energia minima, Emax energia maxima y Ei energia de cada sistema
    global alphaNumber
    # % definir sistemas alphas (mejores). La normalizacion se obtiene con el paso anterior
    global PcentBestFitness
    # NUmero maximo de ciclos que se deben mantener para encontrar GM
    global maxConvergencia
    global reset
    # Varbiales caso calculo local
    global bloque, resto
    # Variables ejecucion
    global job_scheduler, parallel, command

    global shuffleElements

    global KnownPoblation,FillPoblation

    global RunOnNodes
    Big_variable = {}
    PCentCloseness = 1.0
    Pcent1D = 0.1
    Pcent2D = 0.3
    PcentAtomosMutadosMovimiento = 0.3
    PcentToMutate = 0.2
    PcentToCreate =0.1
    PcentBestFitness = 0.5

    alphaNumber = 3
    maxConvergencia = 9
    reset = 0

    shuffleElements = 1
    KnownPoblation = 0      # 0 Poblacion de 0, 1 poblacion Conocida
    FillPoblation = 0       # 0 Rellenar, 1 No rellenar

    RunOnNodes=-1
def is_number(d,n):
    is_number = True
    try:
        num = float(n)
        # check for "nan" floats
        is_number = num == num   # or use `math.isnan(num)`
        if 'Pcent' in d and (num<0 or num>1):
            print("Valor de ",d, " fuera de los limites [0,1]\n")
            exit(1)
    except ValueError:
        is_number = False
        print ("Informacion en archivo de variables incorrecta\n",d ,"=", n)
        exit(1)
    return is_number

def formulaQuimicaAHash():
    data = Big_variable["chemical_formula"].split(' ')
    valores = {}
    atomos = 0
    for i in range(len(data)):
        if i%2 == 0:
            valores[data[i]]=int(data[i+1])
            atomos+=int(data[i+1])
        pass
    valores["all"] = atomos
    return valores#["Si"]
def distribucionCalculos():
    global bloque, resto
    bloque = int(int(Big_variable["numb_conf"])/int(Big_variable["parallel"]))
    resto =int(Big_variable["numb_conf"])%int(Big_variable["parallel"])
    if(resto!=0):
        bloque+=1
    #return bloque, resto

def establecerVariablesDefault():
    global Pcent1D,Pcent2D,PcentAtomosMutadosMovimiento,PcentToMutate,PcentToCreate,PcentBestFitness,maxConvergencia,alphanumber,reset, PCentCloseness
    global job_scheduler,command,parallel
    global shuffleElements
    global KnownPoblation,FillPoblation
    global RunOnNodes
    print(Big_variable)

    if "pcent1d" in Big_variable.keys():
        is_number("Pcent1D",Big_variable["pcent1d"])
        Pcent1D = float(Big_variable["pcent1d"])
    if "pcent2d" in Big_variable.keys():
        is_number("Pcent2D",Big_variable["pcent2d"])
        Pcent2D = float(Big_variable["pcent2d"])
    if "pcentatomosmutadosmovimiento" in Big_variable.keys():
        is_number("PcentAtomosMutadosMovimiento",Big_variable["pcentatomosmutadosmovimiento"])
        PcentAtomosMutadosMovimiento = float(Big_variable["pcentatomosmutadosmovimiento"])
    if "pcenttomutate" in Big_variable.keys():
        is_number("PcentToMutate",Big_variable["pcenttomutate"])
        PcentToMutate = float(Big_variable["pcenttomutate"])
    if "pcenttocreate" in Big_variable.keys():
        is_number("PcentToCreate",Big_variable["pcenttocreate"])
        PcentToCreate = float(Big_variable["pcenttocreate"])

    if "pcentcloseness" in Big_variable.keys():
        is_number("PCentCloseness",Big_variable["pcentcloseness"])
        PCentCloseness = float(Big_variable["pcentcloseness"])

    if "pcentbestfitness" in Big_variable.keys():
        is_number("PcentBestFitness",Big_variable["pcentbestfitness"])
        PcentBestFitness = float(Big_variable["pcentbestfitness"])
    
    if "alphanumber" in Big_variable.keys():
        is_number("alphaNumber",Big_variable["alphanumber"])
        alphaNumber = int(Big_variable["alphanumber"])
    if "maxconvergencia" in Big_variable.keys():
        is_number("maxConvergencia",Big_variable["maxconvergencia"])
        maxConvergencia = int(Big_variable["maxconvergencia"])
    if "reset" in Big_variable.keys():
        is_number("reset",Big_variable["reset"])
        reset = int(Big_variable["reset"])

    if "job-scheduler" in Big_variable.keys():
        job_scheduler = Big_variable["job-scheduler"].lower()
    if "parallel" in Big_variable.keys():
        is_number("parallel",Big_variable["parallel"])
        parallel = int(Big_variable["parallel"])
    if "command" in Big_variable.keys():
        command = Big_variable["command"]

    if "shuffleelements" in Big_variable.keys():
        is_number("shuffleElements",Big_variable["shuffleelements"])
        shuffleElements = int(Big_variable["shuffleelements"])

    if "knownpoblation" in Big_variable.keys():
        is_number("KnownPoblation",Big_variable["knownpoblation"])
        KnownPoblation = int(Big_variable["knownpoblation"])
    if "fillpoblation" in Big_variable.keys():
        is_number("FillPoblation",Big_variable["fillpoblation"])
        FillPoblation = int(Big_variable["fillpoblation"])
    if "runonnodes" in Big_variable.keys():
        RunOnNodes = Big_variable["runonnodes"]
##
##RunOnNodes
# VERIFICAR QUE COMMAND EXISTE SI JOB-SCHULDER ES LOCAL