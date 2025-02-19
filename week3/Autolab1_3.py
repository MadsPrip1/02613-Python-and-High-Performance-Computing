import numpy as np
import sys
from time import perf_counter

numbers = int(sys.argv[1])

SIZE = np.logspace(1, 4.5)
mat = np.random.rand(SIZE, SIZE)

t_start = perf_counter()
for _ in range(numbers):
    double_column = 2 * mat[:, 0]
t_end = perf_counter()
print(f'Time to exicute the double column is {t_end - t_start} for {numbers} numbers')

t_start = perf_counter()
for _ in range(numbers):
    double_row = 2 * mat[0, :]
t_end = perf_counter()
print(f'Time to exicute the double row is {t_end - t_start} for {numbers} numbers')
