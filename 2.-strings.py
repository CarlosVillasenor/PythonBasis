# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Brad"
age = 37

# Concatenate

print('Hello I am ' + name + 'and I am ' + str(age))

# String Formatting

# Arguments by position

print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My Name is {name} and I am {age}'.format(name='Carlos', age=28))

# F-Strings (only in 3.6+)

print(f'My name is {name} and I am {age}')

# String Methods

s = 'Hello there world'
## Capitalize first letter
print(s.capitalize())
## Make all uppercase
print(s.upper())
## Make all lower
print(s.lower())
## Swap case 
## Makes uppercase lowecase and vice versa
print(s.swapcase())
## Get lenght of string
print(len(s))
## Replace 
print(s.replace('world', 'everyone'))
## Count certain string inside other string
sub = "h"
print(s.count(sub))
## Split into a list(array in js)
print(s.split())
## Find Index of string
print(s.find('r'))
## Starts with ?
print(s.startswith('Hello'))
## Ends with ?
print(s.endswith('d'))
## Is all alphanumeric ?
print(s.isalnum())
## Is all alphabetic ?
print(s.isalpha())
## Is all numeric ?
print(s.isalnum())