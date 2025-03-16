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
OUTPUT_FILE="timing_results.txt"
> $OUTPUT_FILE  

for n_proc in {1..10}; do
    echo "Running with $n_proc processes..." | tee -a $OUTPUT_FILE
    
    # Run and measure execution time for parallel implementations
    { time python chunked_parallel.py $n_proc; } 2>> $OUTPUT_FILE
    { time python fully_parallel.py $n_proc; } 2>> $OUTPUT_FILE
done

# Run the serial implementation (only once, since it's not parallel)
echo "Running serial implementation..." | tee -a $OUTPUT_FILE
{ time python fully_serial.py; } 2>> $OUTPUT_FILE