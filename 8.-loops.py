# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary,
# a set, or a string).

people = ['John','Carlos','Javier','Jordi']

# Simple for loop
# for person in people:
#    print('Current person: ' , person)

# Break out
# for person in people:
#    if person == 'Javier':
#        break
#    print('Current person: ' , person)

# Continue
# it means that it will not execute our code block and will continue to the nex iteration
# for person in people:
#    if person == 'Javier':
#        continue
#    print('Current person: ' , person)

# Range
#for i in range(len(people)):
#    print('Current Person: ', people[i])

#for i in range(0, 11):
#    print('Number', i)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print('Count:', count)
    count += 1