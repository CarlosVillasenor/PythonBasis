# Python has functions for creating, reading, updating, and deleting files.

# Open a file
# w as a parameter allow us to write in the created file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name', myFile.name)
print('Is closed', myFile.closed)
print('Opening mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write(' and I also like PHP')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
# text value will be the first 10 characters of myFile
text = myFile.read(10)
print(text)