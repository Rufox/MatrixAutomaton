import subprocess as sb
import Var as var
import os

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
    
    if var.Big_variable["software"].lower() == "orca":
        slrm.write("#SBATCH --nodes="+proc+"\n")
        slrm.write("#SBATCH --ntasks-per-node="+proc+"\n")
        slrm.write("#SBATCH --output="+nombre+".out"+"\n")
        slrm.write("\nml ORCA/4.2.1-OpenMPI-3.1.4\n")
        slrm.write("\n${EBROOTORCA}/orca "+str(file)+"\n")
    elif var.Big_variable["software"].lower() == "gaussian":
        slrm.write("#SBATCH --nodes=1\n")
        slrm.write("#SBATCH -c "+proc+"\n")
        slrm.write("#SBATCH --output=/dev/null\n")
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
    slrm.write("#$ -S /bin/bash\n")
    if var.Big_variable["software"].lower() == "orca":
        slrm.write("#$ -o "+nombre+".out"+"\n")
        slrm.write("\nml ORCA/4.1.1-OpenMPI-3.1.3\n\n")
        slrm.write("\nsrun orca "+str(file)+"\n")
    elif var.Big_variable["software"].lower() == "gaussian":
        slrm.write("#$ -o /dev/null\n")
        slrm.write("\nsource setg16Var\n\n")
        slrm.write("\ng16 "+str(file)+"\n")
    else:
        print("Programa no soportado")
    slrm.close()
    state = sb.Popen(["qsub",nombre+".slrm"])

def LocalMode(name,file, LANZ):
    print(LANZ)
    if(os.path.exists("BATCH-"+name+str(LANZ)+".slrm")):
        slrm = open("BATCH-"+name+str(LANZ)+".slrm","a")
    else:
        slrm = open("BATCH-"+name+str(LANZ)+".slrm","w+")
        slrm.write("#!/bin/bash \n")
    slrm.write(var.Big_variable["command"]+" "+file+"\n")

def SendLocal(name,LANZ):
    #state = sb.Popen(["sh","BATCH-"+ name+str(LANZ)+".slrm","&"])
    #stdout, stderr = state.communicate()
    #print(stdout, stderr)
    #print(state.returncode )
    if(os.path.exists("BATCH-"+ name+str(LANZ)+".slrm")):
        #try:
        #sb.check_output(["sh","BATCH-"+ name+str(LANZ)+".slrm","&"])
        state = sb.Popen(["sh","BATCH-"+ name+str(LANZ)+".slrm","&"],stdout=sb.PIPE,stderr=sb.PIPE)
        #stdout, stderr = state.communicate()
        #print(state.returncode)
        #print(stderr, stdout)
        #if(stderr == None):
        #print(stderr)
    #except sb.CalledProcessError  as e:
        #   print("Error Catastrofico\n")
        #   exit(1)
        #raise e