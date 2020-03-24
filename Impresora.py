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
			print "No XYZ"
	outs = glob.glob("Child*")
	for data in outs:
		try:
			os.remove(data)
			pass
		except:
			print "No OUTS"
	mut = glob.glob("Mut*")
	for data in mut:
		try:
			os.remove(mut)
			pass
		except:
			print "No MUT"
	com = glob.glob("*.com")
	for data in xyz:
		try:
			os.remove(com)
			pass
		except:
			print "No Coms"
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
	input.write("\n")		#Porque Gaussian es espcial
	input.close()

def escribirArchivoXYZ(name, numeroAtomo, title, coordsList):
	input = open(name+".xyz","a")
	input.write(str(numeroAtomo)+"\n")
	input.write(title+"\n")
	for line in coordsList:
		#print (line)
		#line.pop()
		#input.write(' '.join(map(str, line))+"\n")
		input.write(line[0]+"\t"+str(line[1])+"\t"+str(line[2])+"\t"+str(line[3])+"\n")
def escribirArchivoLog(info):
	input = open("LOGS","a")
	input.write(str(info)+"\n")
	pass