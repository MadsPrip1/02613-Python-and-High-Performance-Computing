import sys

list_of_strings = sys.argv[1:]
list_of_even_numbers = [x for x in list_of_strings if float(x) % 2 == 0]
print(list_of_even_numbers)