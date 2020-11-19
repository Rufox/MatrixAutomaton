import Var as var
import numpy as np
import os
import glob

def crearArchivos():
    xyz = glob.glob("*.xyz")
    for data in xyz:
        try:
            os.remove(data)
            pass
        except:
            print("No XYZ")
    outs = glob.glob("Child*")
    for data in outs:
        try:
            os.remove(data)
            pass
        except:
            print("No OUTS")
    mut = glob.glob("Mut*")
    for data in mut:
        try:
            os.remove(mut)
            pass
        except:
            pass
    com = glob.glob("*.com")
    for data in com:
        try:
            os.remove(com)
            pass
        except:
            pass
    open("LOGS","w+")

def escribirInputGaussian(name,number,origincoords):
    coordsList = np.array([[row[0],row[1], row[2], row[3]] for row in origincoords])
    input = open(name+str(number)+".com","w+")
    
    #print (var.Big_variable)
    input.write("%NProc="+var.Big_variable["core"]+"\n")
    input.write("%mem="+var.Big_variable["memory"]+"GB\n")
    input.write("#"+var.Big_variable["header"]+"\n\n")
    input.write("Automatic Input "+name+" "+str(number)+"\n\n")
    input.write(var.Big_variable["charge_multi"]+"\n")
    for line in coordsList:
        input.write(' '.join(map(str, line))+"\n")
    input.write("\n")       #Porque Gaussian es espcial
    input.close()

def escribirInputOrca(name,number,origincoords):
    coordsList = np.array([[row[0],row[1], row[2], row[3]] for row in origincoords])
    input = open(name+str(number)+".inp","w+")
    
    #print (var.Big_variable)
    input.write("%PAL NPROC "+var.Big_variable["core"]+" END\n")
    if var.Big_variable["charge_multi"][2]=="1":
        input.write("! RKS "+var.Big_variable["header"]+"\n")
    else:
        input.write("! UKS "+var.Big_variable["header"]+"\n")
    input.write("%GEOM\n")
    input.write("MAXITER 512\n")
    input.write("END\n")
    #input.write("Automatic Input "+name+" "+str(number)+"\n")
    input.write("* xyz "+var.Big_variable["charge_multi"]+"\n")
    for line in coordsList:
        input.write(' '.join(map(str, line))+"\n")
    input.write("*")       # input.write("\n")#Porque Gaussian es espcial
    input.close()

def escribirInput(name,number,origincoords):
    print(name,number,origincoords)
    if var.Big_variable["software"].lower() == "orca":
        escribirInputOrca(name,number,origincoords)
    elif var.Big_variable["software"].lower() == "gaussian":
        escribirInputGaussian(name,number,origincoords)
    else:
        print("Software no disponible, elegir orca o gaussian")

# Escribe solo 1 sistema a un archivo xyz, si el archivo xyz se llama varia veces se agregaran mas sistemas.
def escribirArchivoXYZ(name, numeroAtomo, title, coordsList):
    input = open(name+".xyz","a")
    input.write(str(numeroAtomo)+"\n")
    input.write(title+"\n")
    for line in coordsList:
        input.write(line[0]+"\t"+str(line[1])+"\t"+str(line[2])+"\t"+str(line[3])+"\n")

# Impresion LOG, funcion simple que imprime cualquier informacion en un archivo de texto
def escribirArchivoLog(info):
    input = open("LOGS","a")
    input.write(str(info)+"\n")
    pass
