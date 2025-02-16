import sys
import numpy as np
from time import perf_counter

# The input to the program is the path to a file containing a numpy matrix and an integer p.
# python program.py path/to/data.txt p

path_to_matrix = sys.argv[1]
matrix = np.load(path_to_matrix)
matrix_multiple = matrix
p = int(sys.argv[2])

t_start = perf_counter()
for _ in range(p):
    matrix_multiple = matrix_multiple @ matrix 
t_end = perf_counter()

np.save('matrix_multiple', matrix_multiple)
print(t_end - t_start)