#!/usr/bin/python


GaussianCall = "Gaussian16"
extension = "log"
NumberConfig=177
Numero=20
# Diccionarios, no cambiar
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

#atomic_number = {H:1,He:2,Li:3,Be:4}

#Porcentaje de atomos que sufriran unmovimiento aleatorio como mutacion.
#Valores entre 0 y 1
PcentAtomosMutadosMovimiento = 0.3

# NUmero maximo de ciclos que se deben mantener para encontrar GM
maxConvergencia = 9

# % de N a mutar (patada e intercambio)
PcentToMutate = 0.2
# % de N a recombinar. NOT USED
PcentToRecombine =0.2
#
#PcentToCreate =0.6

#Fitness
# Valos alpha, no tengo idea que significa, copiado textual del programa anterior
# FOrmula mejor = exp ^ (-alphaNumber * prob); donde prob = (Ei-Emin) / (Emax -Emin) donde Emin energia minima, Emax energia maxima y Ei energia de cada sistema
alphaNumber = 3
# % definir sistemas alphas (mejores). La normalizacion se obtiene con el paso anterior
PcentBestFitness = 0.5



# Funciones de programa NO BORRAR NI EDITAR
def init():
	global Big_variable
	Big_variable = {}
	
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