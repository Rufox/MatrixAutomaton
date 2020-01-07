
import Lector
import Var as var

var.init()
Lector.leerArchivoParametros()


print list(var.Big_variable)

print var.Big_variable["numb_conf"]

mio = Lector.obtenerCoordenadaGaussian("Cell2D_1_000007.out")

print mio