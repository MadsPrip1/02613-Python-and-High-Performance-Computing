#!/bin/bash

### -- set the job Name -- 
#BSUB -J time_test1_2

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 4

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=512MB]"

### -- select the machine to be XeonGold6226R --
#BSUB -R "select[model==XeonGold6226R]"

### -- ask for number of cores (default: 1) -- 
#BSUB -n 1

### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o bash_output/time_test1_2_%J.out
#BSUB -e bash_output/time_test1_2_%J.err

### -- Need to activate the python environment --
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

### -- run in the job --
### -- python program.py num_of_iterations -- 
python Autolab1_1.py 1000
