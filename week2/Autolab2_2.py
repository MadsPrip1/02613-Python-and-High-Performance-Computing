import sys
import numpy as np

# Create a array from the input numbers and print the norm of the array.
# The following is the input to the program, remember that the numbers will be inserted as strings
# python program..py 1 2 3 4 5                                          

number_of_strings = sys.argv[1:]
number_np_array = np.array([float(x) for x in number_of_strings])
print(np.linalg.norm(number_np_array))