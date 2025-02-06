#!/bin/bash

### -- set the job Name -- 
#BSUB -J sleeper

### -- specify queue --
#BSUB -q hpc

### -- set walltime limit: hh:mm -- 
#BSUB -W 2

### -- specify that we need 512MB of memory per core/slot --
#BSUB -R "rusage[mem=512MB]"

### -- select the machine to be XeonE5 2660v3 --
#BSUB -R "select[model==XeonE5_2660v3]"

### -- ask for number of cores (default: 1) -- 
#BSUB -n 16

### -- specify that the cores must be on the same host -- 
#BSUB -R "span[hosts=1]"

### -- Specify the output and error file. %J is the job-id -- 
### -- -o and -e mean append, -oo and -eo mean overwrite -- 
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err

### -- send notification at start to email --
#BSUB -B

### -- send notification at completion to email --
#BSUB -N

### -- display information about the CPU architecture --
lscpu

sleep 60

