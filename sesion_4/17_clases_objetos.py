"""
CLASES Y OBJECTOS

En la programacion orientada a objetos diria que tenemos 4 conceptos fundamentales:
- Class
- Object
- Attributes
- Methods


CLASS
- coleccion de objectos -> template (recipe) para crear nuevos objetos
- Una clase contiene el prototipo a partir del cual se crean los objetos
- Es una entidade logica que contiene atributos y metodos. 
"""

# %% 
# Creating class
class User:
    print("Esta es una clase User")

user_1 = User()
user_2 = User()

print(User)
# <class '__main__.User'>
print(user_1)
#<__main__.User object at 0x10a5e13d0>

print(user_2)
#<__main__.User object at 0x10a54f640>
# %%

# Attributes (Atributos)
# los atributos son como variables que pertenecen a una determinada clase y/o objetos
# son siempre publicos 
# syntax: miobjeto.miatributo
# pueden ser definidos cuando se crea el objeto (clase) o despues que el objeto es creado

class User():
    print("Esta es una clase User")

user_1 = User()
# Esta es una clase User

# creating an attribute name a este objeto
user_1.name = "Roberto"
print(user_1.name)
# Roberto

user_2 = User()
user_2.name
# AttributeError: 'User' object has no attribute 'name'
user_2.age = 30
user_2.age
# 30

user_1.age
#AttributeError: 'User' object has no attribute 'age'

# %%
class User():
    print("Esta es una clase User")
    # Definicion de un atributo global (clase)
    name = "Roberto"
    age = 30

user_1 = User()
user_2 = User()

print(user_1.name, user_1.age)
print(user_2.name, user_2.age)
#Roberto 30
#Roberto 30

user_1.name = "Joaquin"
print(user_1.name, user_1.age)
# Joaquin 30
# %%
# Contructores - init()
# __init__(): asignar atributos de los objetos en el momento de su creacion

class User:
    print("Esta es una clase User")
    game = "SimCity"

    # Metodo de inicialization __inti__
    def __init__(self,input_name="Unknown",input_age=None):
        self.name = input_name
        self.age = input_age
        self.locality = "Madrid"

user_1 = User()
#TypeError: __init__() missing 2 required positional arguments: 'input_name' and 'input_age'

user_1 = User(input_name="Roberto",input_age=30)
user_2 = User(input_name="Joaquin",input_age=28)
print(user_1.name, user_1.age)
print(user_2.name, user_2.age)
#Roberto 30
#Joaquin 28

user_1.locality
# Madrid
user_1.game
# 'SimCity'

# %%
class User:
    def __init__():
        self.name = "user"

# %%
# METHODS - METODOS
class User():
    # Class attributes
    game = "SimCity"

    # Metodo de inicializacion
    # -- atributos de la instancia
    def __init__(self, name:str, age:int, city:str):
        self.name = name
        self.age = age
        self.city = city
    
    # Metodo general - greeting
    def say_hello(self):
        print(f"Hello! My name is {self.name}")
    
    def repeat(self,x):
        print(x)

user_1 = User("roberto",30,"madrid")
print(user_1.name, user_1.age, user_1.city)
print(user_1.say_hello())
#roberto 30 madrid
#Hello! My name is roberto

user_1.repeat("Hi")
# Hi
# %%
class User():
    # Class attributes
    game = "SimCity"

    # Metodo de inicializacion
    # -- atributos de la instancia
    def __init__(self, name:str, age:int, city:str):
        self.name = name
        self.age = age
        self.city = city
    
    # Metodo general - greeting
    def say_hello(self):
        print(f"Hello! My name is {self.name}")
    
    # Static method 
    @staticmethod
    def repeat(text):
        print(f"This is your text: {text}")

user_1 = User("roberto",30,"madrid")
print(user_1.repeat("Hola!!"))
# This is your text: Hola!!
# %%
# NESTED METHODS
class User():
    def __init__(self, name:str, age:int, city:str):
        self.name = self._clean_text(name)
        self.age = age
        self.city = self._clean_text(city)
    
    @staticmethod
    def _clean_text(s:str):
        return str(s).strip().capitalize()

user_3 = User("roberto  ",38," MADRID  ")
print(user_3.name,user_3.city)
#Roberto Madrid

# %% Inheritance - Herencia
"""
class FirstClass:
    # properties FirstClass

class SecondClass(FirstClass):
    # properties Second Class
"""
class BaseUser:
    game = "SimCity"

    def __init__(self, name:str, age:int, city:str):
        self.name = self._clean_text(name)
        self.age = age
        self.city = self._clean_text(city)

    @staticmethod
    def _clean_text(s:str):
        return str(s).strip().capitalize()

class User(BaseUser):

    def get_name(self):
        return self.name

user_1 = User("roberto  ",38," MADRID  ")
print(user_1.name,user_1.age,user_1.city)
# Roberto 38 Madrid

user_1.get_name()
# 'Roberto'

user_2 = User(name="Joaquin",age=28,city="Barceloa")
#'Joaquin'

user_3 = BaseUser(name="Joaquin",age=28,city="Barcelona")
user_3.get_name()
#AttributeError: 'BaseUser' object has no attribute 'get_name'
# %%
class BaseUser:
    game = "SimCity"

    def __init__(self, name:str, age:int, city:str):
        self.name = self._clean_text(name)
        self.age = age
        self.city = self._clean_text(city)

    @staticmethod
    def _clean_text(s:str):
        return str(s).strip().capitalize()

class User(BaseUser):

    def __init__(self,name,age,city,level):
        self.level = level
        # Invoking del Parent Class __init__
        BaseUser.__init__(self,name,age,city)

    def get_name(self):
        return self.name

user_1 = User("roberto  ",38," MADRID  ","beginner")
user_1.level 
# beginner

# %% 
# Destructor
class User:
    def __init__(self, name):
        self.name = name
        print(f"Your name is {self.name}")
    
    # Adding destructor
    def __del__(self):
        print("User deleted.")

user_1 = User("Roberto")
# Your name is Roberto

del user_1
#User deleted.

print(user_1)
#NameError: name 'user_1' is not defined
# %%

# CLASES ABSTRATAS Y IMPLEMENTACION DE INTERFACES
# Defining abstract class
from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def get_age(self):
        pass

# %%
from abc import ABC, abstractmethod

class Human(ABC):
    @abstractmethod
    def get_age(self):
        pass

# Definir las sub-clases
class Child(Human):
    # overwrite abstract methods
    def get_age(self):
        print("I'm 7 years old")

class Adult(Human):
    # overwrite abstract methods
    def get_age(self):
        print("I'm 47 years old")

child_1 = Child()
child_1.get_age()
# I'm 7 years old

adult_1 = Adult()
# adult_1.get_age()

human = Human()
#TypeError: Can't instantiate abstract class Human with abstract methods get_age
# %%
