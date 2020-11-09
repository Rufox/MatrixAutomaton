import subprocess as sb
import Var as var

# Llamada a sistema cluster,
def envioCluster(gaussian, nombre, file, proc, cola):
    #state = sb.Popen(["Gaussian16.b01","d","Si1.com","4","test"])
    #state = sb.Popen([params])
    #print gaussian,nombre,str(file),str(proc),str(cola)
    state = sb.Popen([gaussian,nombre,str(file),str(proc),str(cola)])
    return state

def slurmCluster(nombre, file, proc, cola):
    slrm = open(nombre+".slrm","w+")
    slrm.write("#!/bin/bash \n")
    slrm.write("#SBATCH --job-name="+nombre+"\n")
    slrm.write("#SBATCH --partition="+cola+"\n")
    slrm.write("#SBATCH --nodes=1\n")
    slrm.write("#SBATCH -c "+proc+"\n")
    slrm.write("#SBATCH --output=/dev/null\n")
    if var.Big_variable["software"] == "orca":
        slrm.write("\nml ORCA/4.1.1-OpenMPI-3.1.3\n\n")
        slrm.write("\nsrun orca "+str(file)+"\n")
    elif var.Big_variable["software"] == "gaussian":
        slrm.write("\nml g16/B.01\n\n")
        slrm.write("\nsrun g16 "+str(file)+"\n")
    else:
        print("Programa no soportado")
    slrm.close()
    state = sb.Popen(["sbatch",nombre+".slrm"])

def SGECluster(nombre, file, proc, cola):
    #copiar el archivo Gaussian16 aca
    slrm = open(nombre+".slrm","w+")
    slrm.write("#!/bin/bash \n")
    slrm.write("#$ -cwd\n")
    slrm.write("#$ -j y\n")    
    slrm.write("#$ -N "+nombre+"\n")
    slrm.write("#$ -q "+cola+"\n")
    #slrm.write("#SBATCH --nodes=1\n")
    slrm.write("#$ -pe solouno "+proc+"\n")
    slrm.write("#$ -o /dev/null\n")
    slrm.write("#$ -S /bin/bash\n")
    if var.Big_variable["software"] == "orca":
        slrm.write("\nml ORCA/4.1.1-OpenMPI-3.1.3\n\n")
        slrm.write("\nsrun orca "+str(file)+"\n")
    elif var.Big_variable["software"] == "gaussian":
        slrm.write("\nsource setg16Var\n\n")
        slrm.write("\ng16 "+str(file)+"\n")
    else:
        print("Programa no soportado")
    slrm.close()
    state = sb.Popen(["qsub",nombre+".slrm"])