# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Simple  tuple
# fruit_tuple = ('Apple', 'Orange', 'Mango')

# Declare tuple using the constructor
fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))

print(fruit_tuple)

# Get single value
print(fruit_tuple[1])

# Can not change value
#fruit_tuple[1] = 'Graple'

# Tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',)

# Get len of tuple
print(len(fruit_tuple))

# delete a tuple
# del fruit_tuple_2

print(fruit_tuple_2)

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruit_set = {'Apple', 'Orange', 'Mango'}

# members can´t be duplicated
fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

# Check if in set
print('Apple' in fruit_set)

# Add to a set
fruit_set.add('Grape')

# Remove from set
fruit_set.remove('Apple')

# Clear set
fruit_set.clear()

# Delete set
# del fruit_set


print(fruit_set)