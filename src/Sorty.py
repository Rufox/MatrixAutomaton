import glob
import sys
import re
import numpy as np
import cclib
from cclib.parser import Gaussian
from multiprocessing import Pool

# This works with python3.8
# existing code...
hartree2au = 627.509469
ev2hartree = 27.21138511#27.2114#13966

molecules = []
def process_file(file):
    parser = Gaussian(file)
    data = parser.parse()
    #flagFreq = False
    energy = 0
    flagFreq = False
    zpe = None
    eState = None  
    minFreq = None
    pGroup = None
    HOMO = None
    LUMO =None
    GAP = None
    
    if('scfenergies' in dir(data)):
        #print ("Ocurre")
        energy = min(data.scfenergies) / ev2hartree
        min_index = np.argmin(data.scfenergies)
        try:
            opt_coords = data.atomcoords[min_index]
        except IndexError as e:
            print("Caso Especial, Se sugiere revisar Manual {}".format(file))
            opt_coords = data.atomcoords[min_index-1]
            energy = data.scfenergies[-2] / ev2hartree
        #print(data.atomnos)
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if re.search(r"Zero-point correction", line):
                    zpe = float(line.split()[2]) #/ pybel.constants.hartree2au
                    #break
                if re.search(r"The electronic state is", line):
                    eState = line.split()[-1]
                if (re.search(r"Frequencies", line) and flagFreq is False):
                    minFreq = line.split()[2]
                    flagFreq = True
                if re.search(r"Full point group", line):
                    pGroup = line.split()[3]
                if re.search(r"Alpha  occ. eigenvalues", line):
                    try:
                        HOMO = float(line.split()[-1])
                    except ValueError as e:
                        pass
                    LUMOFlag = False
                if (re.search(r"Alpha virt. eigenvalues", line) and LUMOFlag is False):
                    try:
                        LUMO = float(line.split()[4])
                    except ValueError as e:
                        pass
                    LUMOFlag = True
        if HOMO is not None and LUMO is not None:
            GAP = round(((LUMO - HOMO) * 27.2114),4)
        if zpe is not None:
            finalEnergy = energy + zpe
        else:
            finalEnergy = energy
        Name = file
        print("{}\tEnergy {} + {} = {}".format(Name,energy, zpe, finalEnergy), end =" ")
        print("Elec State {}".format(eState), end =" ")
        print("Min Freq {}".format(minFreq), end =" ")
        print("Puntual Group {}".format(pGroup), end =" ")
        print ("HOMO : {}  LUMO {}".format(HOMO, LUMO))
        energy =finalEnergy
        title = "{} H\tMinFreq {}\tSpect {}\tPGroup {}\tGAP {} H\t{}\n".format(round(energy,6),minFreq,eState,pGroup,GAP,Name)
        #print(title)
        return [energy, title, opt_coords, len(opt_coords), data.atomnos]
    else:
        print ( "Calculo {} NO inicio correctamente, ignorado".format(file))


def main(Otype):
    if(Otype == "-o"):
        files = glob.glob("*.out")
    elif (Otype == "-l"):
        files = glob.glob("*.log")
    else:
        print("No format given, use -o or -l to specify\n")
        sys.exit(1)
    
    with Pool() as pool:
        molecules = pool.map(process_file, files)

    if not files:
        print("No files with format specified")
        sys.exit(1)
    molecules = [m for m in molecules if m is not None]
    molecules.sort(key=lambda x: x[0])
    #print(molecules)
    minEnergy = molecules[0][0]

    with open("all_coords.xyz", "w") as f:
        for energy,title ,opt_coords, size, symbol in molecules:
            Kcal = round(((energy - minEnergy) * hartree2au), 4)
            eV      = round(((energy - minEnergy) * 27.2114), 4)
            title = "{} Kcal/mol {} eV ".format(Kcal,eV) + title
            f.write("{}\n".format(size))
            f.write("{}".format(title))
            for i, pos in enumerate(opt_coords):
                f.write("{}\t{}\t{}\t{}\n".format(symbol[i], pos[0], pos[1], pos[2]))


#if __name__ == '__main__':
    

    #print(files)
