import sys
import numpy as np

# Create a matrix from the input numbers and save it to a file.
# The following is the input to the program, remember that the numbers will be inserted as strings
# python program..py 1 2 3 4 5                                          

number_of_strings = sys.argv[1:]
matrix = np.diag([float(x) for x in number_of_strings])
np.save('matrix', matrix)