# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
# person = {
#    'first_name': 'Carlos',
#    'last_name': 'Villaseñor',
#    'age': 30
# }

# Declare a simple dict using a constructor
person = dict(
    first_name='Carlos',
    last_name='Villaseñor',
    age=30
)

# Get single value
# print(person['first_name'])
# print(person.get('last_name'))

# Add key/value
person['phone'] = '22 27 65 59 47'

# Get keys
# print(person.keys())

# Get values
# print(person.items())

# Make copy
person2 = person.copy()
person2['city'] = 'Boston'

# Get length
print(len(person2))
print(person)

# Remove item
del(person['age'])
person.pop('phone')

# Crear the dictionary
person.clear()


# List of dict
people = [
    {'name':'Martha', 'age': 40},
    {'name':'Bob', 'age': 20}
]

print(people[1]['name'])

