#!/bin/bash 
#SBATCH --job-name=MA_H2O
#SBATCH --partition=general
#SBATCH --nodes=1
#SBATCH -c 1	
#SBATCH --output=trash



srun ./Automaton Config.in general

