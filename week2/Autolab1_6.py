import sys

# Print the even numbers from the input list of strings
# The following is the input to the program, remember that the numbers will be inserted as strings
# python program..py 1 2 3 4 5                

list_of_strings = sys.argv[1:]
list_of_even_numbers = [x for x in list_of_strings if float(x) % 2 == 0]
print(list_of_even_numbers)