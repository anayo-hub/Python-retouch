# import datetime
from camelcase import CamelCase


# today = datetime.date.today()

c = CamelCase()

# print(c.hump('hello world'))

# print(today)

class User:
    def __init__(self, name, age, town):
        self.name = name
        self.age = age
        self.town = town

crescent = User( 'anayo crescent', 30, "opi")

print(c.hump(crescent.name))