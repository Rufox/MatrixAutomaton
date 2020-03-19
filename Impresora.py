import Var as var
import numpy as np
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
	input.write("\n")		#Porque Gaussian es espcial
	input.close()

def escribirArchivoXYZ(name, numeroAtomo, title, coordsList):
	input = open(name+".xyz","a")
	input.write(str(numeroAtomo)+"\n")
	input.write(title+"\n")
	for line in coordsList:
		#print (line)
		input.write(' '.join(map(str, line))+"\n")
	