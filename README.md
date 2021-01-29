# AUTOMATON 2.0
El propósito de AUTOMATON 2.0 es encontrar la estructura más estable de un clúster atómico o molecular desde el punto de vista energético, encontrando el mínimo global mediante la exploración estocástica de la Superficie de Energía Potencial de estas estructuras mediante optimización, utilizando métodos *ab initio* químico computacionales. Con la fórmula química de un clúster, entregada por el usuario, se encuentran los mínimos energéticos locales, el mínimo global y se ordenan estos mínimos de manera decreciente. Esta es una versión actualizada de su antecesor [AUTOMATON](https://github.com/HumanOsv/Automaton "AUTOMATON"), se utiliza un algoritmo híbrido que combina la teoría de Autómata Celular para la generación de población inicial determinando el conjunto de vecindarios con un algoritmo de dibujo de círculo de punto medio, la representación del autómata se realiza con matrices de 1, 2 y 3 dimensiones y el manejo de éstas es soportado por la librería NumPy de Python, especializada en el cálculo numérico y el análisis de datos. Se combina lo anterior con un algoritmo genético que realiza operaciones de cruzamiento y mutaciones por desplazamiento y permutación de átomos. Esta nueva versión se diseñó y codificó con el paradigma de Programación Orientada a Objetos y se realizó el cambio del lenguaje de programación de Perl a Python, logrando reducir el tiempo de ejecución en un 67 % aproximadamente en comparación con el software original.

## Requisitos
+ AUTOMATON soporta sistemas de gestión de trabajos para clústeres computacionales: SLURM Workload Manager y Sun Grid Engine (SGE).
+ El programa está escrito en el lenguaje computacional Python en sus versiones 2.7 y 3.5.
+ Para la optimización geométrica local y cálculos de energía se utiliza el software de uso comercial para química teórica Gaussian 16, el uso de este software está restringido a los usuarios que dispongan de una licencia válida para la versión de Gaussian y será necesaria para cualquiera de los Sistemas Operativos soportados. En caso de no poseer licencia para Gaussian, se puede utilizar ORCA, que no necesita una licencia pagada para ser ejecutado.

## Archivos de entrada
Config.in es el archivo de configuración, desde donde se obtienen las variables a utilizar por AUTOMATON y por Gaussian/ORCA cuando sea necesario. La mayoría de las variables de este archivo se mantienen iguales independiente del grupo atómico a definir, las variables que deben cambiarse en el archivo de entrada son:
+ Número de estructuras (5N, N = cantidad de átomos). Por ejemplo, si N = 12:
```plain
numb_conf = 60
```
+ Sistema de gestión de trabajos (slurm, sge, local):
```plain
job-scheduler = slurm
```
+ Fórmula química para el sistema:
```plain
chemical_formula = B 8 Be 4
```
+ Software que será utilizado (gaussian u orca):
```plain
software = gaussian
```
+ Procesador y memoria (GB) que será utilizado para cada cálculo:
```plain
core = 4 
memory = 4
```
+ Carga y multiplicidad del candidato (separados por un espacio):
```plain
charge_multi = 0 1
```
+ Palabras clave para Gaussian (header de Gaussian):
```
header = PBE1PBE/SDDAll scf=(maxcycle=512) opt=(cartesian,maxcycle=512)
```

## Archivos de salida
Luego de una ejecución exitosa del programa, se generarán varios archivos de salida en su directorio de trabajo:
+ 01Finalscoords.xyz: Archivo de formato XYZ que entrega las coordenadas finales de cada especie ordenado de mayor a menor energía.
+ Original\*D_i_j: Población inicial creada con el programa de matrices.
	+ \*= cantidad de dimensiones (1, 2 o 3).
	+ i = ciclo.
	+ j = enumeración de conformación.
+ Child_i_j: Se generan con la recombinación del sistema. Se crean a partir de los archivos Original*D_i_j
+ Mutación:
	+ MutD_i_j: Mutación de desplazamiento.
	+ MutI_i_j: Mutación de tipo intercambio.
+ Los archivos Original, Child y MutD/MutI tienen 3 extensiones diferentes:
	+ archivo.com Archivo de entrada de gaussian, coordenadas.
	+ archivo.slrm: Archivo de entrada del cluster.
	+ archivo.log: Archivo de salida de gaussian.
    \end{itemize}
+ Precoords_i.xyz: Archivo de formato xyz con las estructuras no optimizadas por ciclo.
+ PostCoords_i.xyz: Archivo de formato xyz con las estructuras optimizadas localmente por ciclo.
+ LOGS: Archivo de registro de la ejecución del programa. Aquí se registra la fecha y hora de inicio y término de ejecución del programa, los ciclos y estado de convergencia y la información sobre las energías mínimas encontradas y el archivo donde se encontró.
