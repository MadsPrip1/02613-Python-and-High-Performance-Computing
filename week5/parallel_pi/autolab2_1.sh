#!/bin/bash
### -- set the job Name -- 
#BSUB -J parallel_test

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 20

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=1GB]"

### -- select the machine to be XeonGold6226R --
#BSUB -R "select[model==XeonE5_2650v4]"

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

lscpu


### -- run in the job --
### Use the time command below to time how long time it takes the script to be executed
time python fully_serial.py 1
time python chunked_parallel.py 1
time python fully_parallel.py 1

time python fully_serial.py 2
time python chunked_parallel.py 2
time python fully_parallel.py 2

time python fully_serial.py 3
time python chunked_parallel.py 3
time python fully_parallel.py 3

time python fully_serial.py 4
time python chunked_parallel.py 4
time python fully_parallel.py 4

time python fully_serial.py 5
time python chunked_parallel.py 5
time python fully_parallel.py 5

time python fully_serial.py 6
time python chunked_parallel.py 6
time python fully_parallel.py 6

time python fully_serial.py 7
time python chunked_parallel.py 7
time python fully_parallel.py 7

time python fully_serial.py 8
time python chunked_parallel.py 8
time python fully_parallel.py 8

time python fully_serial.py 9
time python chunked_parallel.py 9
time python fully_parallel.py 9

time python fully_serial.py 10
time python chunked_parallel.py 10
time python fully_parallel.py 10

