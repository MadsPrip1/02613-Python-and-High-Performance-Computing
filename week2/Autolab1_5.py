import sys

file_path = sys.argv[0]

list_of_str = sys.argv[1:] # The input is by deafult strings (the first element is the name of the file)
list_of_numbers = [float(string) for string in list_of_str] # Convert strings to float 
mean = sum(list_of_numbers)/len(list_of_numbers)

if mean > 5: # Calculate the mean
    print(f'{mean} Pass')
else:
    print(f'{mean} Fail')