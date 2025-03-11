#!/bin/bash
### -- set the job Name -- 
#BSUB -J parallel_test

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 2

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=1GB]"

### -- select the machine to be XeonGold6226R --
#BSUB -R "select[model==XeonGold6226R]"

### -- ask for number of cores (default: 1) -- 
#BSUB -n 10

### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o bash_output/parallel_test_%J.out
#BSUB -e bash_output/parallel_test_%J.err

### -- Need to activate the python environment --
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

### -- run in the job --
### Use the time command below to time how long time it takes the script to be executed
time python chunked_parallel.py
time python fully_parallel.py
time python fully_serial.py

