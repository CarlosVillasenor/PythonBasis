# A module is basically a file containing a set of functions to include in your application.
# There are core python modules, modules you can install using the pip package manager (including Django)
# as well as custom modules

# Core modules
from datetime import date
import time

# Pip modules
import camelcase

# Custom modules
# we are importing validator from validator.py
from validator import validate_email

today = date.today()
print(today)

timestamp = time.time()
print(timestamp)

# Camelcase will turn every first letter of every world camelcase
camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Not an Email')
