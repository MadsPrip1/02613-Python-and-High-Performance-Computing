#!/bin/bash

### -- set the job Name -- 
#BSUB -J multiplier

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 2

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=512MB]"

### -- select the machine to be XeonE5 2660v3 --
#BSUB -R "select[model==XeonE5_2660v3]"

### -- ask for number of cores (default: 1) -- 
#BSUB -n 1

### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o bash_output/multiplier_%J.out
#BSUB -e bash_output/multiplier_%J.err

### -- send notification at start to email --
#BSUB -B

### -- send notification at completion to email --
#BSUB -N

### -- display information about the CPU architecture --
lscpu

### -- Need to activate the python environment --
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

### -- run in the job --
### -- python program.py path/to/data.txt p -- 
python Autolab2_5.py matrix2_6.npy 1
