# A List is a collection which is ordered and changeable. Allows duplicate members.
# In Javascript this are called Arrays

# Create a  list
# numbers = [1,2,3,4,5]

# Declare a list using a constructor

numbers = list((1, 2, 3, 4, 5))
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(type(numbers))
# Get value of element inside an array
print(fruits[0])

# Get len
print(len(fruits))

# Append to list, like 'push' in Javascript
fruits.append('Mangos')

# Remove from list, like 'pop' in Javascript
fruits.remove('Grapes')

# Insert into position, similar to 'splice' in Javascript
fruits.insert(2, 'Strawberries')

# Remove from certain position, similar to 'splice' in Javascript
fruits.pop(3)

# Reverse list 
fruits.reverse()

# Sort list alphabetically
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
