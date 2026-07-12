# import datetime
# from camelcase import CamelCase


# today = datetime.date.today()

# c = CamelCase()

# print(c.hump('hello world'))

# print(today)

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    def greeting(self):
        return  f'welcome my name is {self.name}, i am {self.age} : email is  {self.email}'
    
class Customer(User):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0
    
    def set_balance(self, balance):
        self.balance = balance 
        
    # def greeting(self):
    #     return  f'welcome my name is {self.name} i am {self.age} : email is  {self.email} and my balance is {self.balance}'

# init an user obj
crescent = User( 'anayo crescent', 32, "anayocrescent@gmail.com")

# init a customer obj
janet = Customer('Janet medea', 37, 'traversy@gmail.com')

janet.set_balance(500)


print(janet.greeting())


print(crescent.greeting())


