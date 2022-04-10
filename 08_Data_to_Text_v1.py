# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename: ")

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item)

# close file
f.close()