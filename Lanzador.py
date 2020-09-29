import subprocess as sb

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
    slrm.write("\nml g16/B.01\n\n")

    slrm.write("\nsrun g16 "+str(file)+"\n")
    slrm.close()
    state = sb.Popen(["sbatch",nombre+".slrm"])