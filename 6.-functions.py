# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# Create a function,
# It has a default value passed in the parameters


def sayHello(name='Sam'):
    """
    Prints Hello and the name parameter.
    """
    print('Hello ' + name)


sayHello('Carlos')

# Return value


def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(9,1))

numSum = getSum(7,9)
print(numSum)

def addOneToNum(num):
    num += 1
    return num

num = 6
new_num = addOneToNum(num)
print(new_num)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

getSumLambda = lambda num1, num2 : num1 + num2
print(getSumLambda(3,9))

addOneToNum = lambda num : num + 1
print(addOneToNum(10))