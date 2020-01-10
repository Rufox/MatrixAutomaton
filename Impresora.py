import Var as var

def escribirInputGaussian(name,number,coordsList):
	input = open(name+str(number)+".com","w+")
	
	print (var.Big_variable)
	input.write("%NProc="+var.Big_variable["core"]+"\n")
	input.write("%mem="+var.Big_variable["memory"]+"GB\n")
	input.write("#"+var.Big_variable["header"]+"\n\n")
	input.write("Automatic Input "+name+" "+str(number)+"\n\n")
	input.write(var.Big_variable["charge_multi"]+"\n")
	for line in coordsList:
		print (line)
		input.write(' '.join(map(str, line))+"\n")
	input.write("\n")		#Porque Gaussian es espcial
	input.close()

def escribirArchivoXYZ(name, numeroAtomo, title, coordsList):
	input = open(name+".xyz","a")
	input.write(str(numeroAtomo)+"\n")
	input.write(title+"\n")
	for line in coordsList:
		print (line)
		input.write(' '.join(map(str, line))+"\n")
	