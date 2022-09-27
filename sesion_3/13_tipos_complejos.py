# TRABAJANDO CON LISTS, DICTIONARIES, TUPLES, SETS

"""
LISTAS (Lists)
"""

# %%
mi_lista = ["Hello", 1, 1.5, True]
print(type(mi_lista))
print(mi_lista)

for element in mi_lista:
    print(type(element))
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# %%
# Acceder a un elemento(s) en una lista 
objects = ["coche","pelota","ordenador","silla"]
first_element = objects[0]
last_element = objects[-1]
print(f"{first_element} is my First Element.")
print(f"{last_element} is my Last Element.")
#coche is my First Element.
#silla is my Last Element.
# %%
objects = [
    ["coche","pelota","ordenador","silla"],
    [1,2,3]
]
print(len(objects))
# 2

first_element = objects[0]
last_element = objects[-1]
print(f"{first_element} is my First Element.")
print(f"{last_element} is my Last Element.")
#['coche', 'pelota', 'ordenador', 'silla'] is my First Element.
#[1, 2, 3] is my Last Element.

objects[0][-1]
#'silla'

objects[0][-1][-1]
# a
# %%
"""
SLICING
[:] -> [start:end:step]
"""
list_numbers = list(range(10))
print(list_numbers[:])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_numbers[2:-1])
#[2, 3, 4, 5, 6, 7, 8]

print(list_numbers[2::3])
#[2, 5, 8]

print(list_numbers[::-1])
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# %%
"""
MODIFICAR UNA LISTA
"""
list_numbers = list(range(10))

list_numbers[0] = -1
list_numbers[-1] = 100
print(list_numbers)
# [-1, 1, 2, 3, 4, 5, 6, 7, 8, 100]

# Ejemplo - ErrorIndex 
list_numbers[20] = "a"
#IndexError: list assignment index out of range
# %%
# Modificar elementos a traves del slicing
numbers = [1,2,3,4]
numbers[1:3] = [-10,-11]
print(numbers)
# [1, -10, -11, 4]

numbers = [1,2,3,4]
numbers[1:3] = [-10,-11, -1,-1]
print(numbers)
# [1, -10, -11, -1, -1, 4]
# %%

"""
METODOS - LISTAS
"""

# APPEND: list.append()
# añadir un elemento al final de la lista

mi_lista = ["Hello", 1, 1.5, True]
element_to_append = "Roberto"

mi_lista.append(element_to_append)
print(mi_lista)
# ['Hello', 1, 1.5, True, 'Roberto']
# %%
lista_numbers = [1,2,15,32,21,27,18,43]
numeros_pares = []

for number in lista_numbers:
    if number % 2 == 0:
        print(f"Numero par encontrado: {number}")
        numeros_pares.append(number)

print(f"Final list: {numeros_pares}")
#Numero par encontrado: 2
#Numero par encontrado: 32
#Numero par encontrado: 18
#Final list: [2, 32, 18]
# %%
# insert() -> añadir un elemento en una posicion determinada
lista_numbers = [1,2,15,32,21,27,18,43]
lista_numbers.insert(1,"Hello")
print(lista_numbers)
# [1, 'Hello', 2, 15, 32, 21, 27, 18, 43]
# %%
# Combinar listas +/+=, extend()

lista_a = ["A","B","C"]
lista_b = ["D","E"]

lista_c = lista_a + lista_b
print(lista_c)
# ['A', 'B', 'C', 'D', 'E']

lista_a.extend(lista_b)
print(lista_a)
#['A', 'B', 'C', 'D', 'E']
# %%
# Eliminar elementos
# del / remove
numbers = [1,2,3,4]
del numbers[-1]
print(numbers)
# [1, 2, 3]

del numbers[20]
#IndexError: list assignment index out of range
# %%
numbers = [1,2,3,4]
numbers.remove(3)
print(numbers)
#[1, 2, 4]
numbers.remove(-1)
#ValueError: list.remove(x): x not in list


# %%
mi_lista = [1,2,2,2,3,4]
mi_lista.remove(2)
mi_lista
# [1, 2, 2, 3, 4]

# %%
# pop() -> te deja sacar un elemento de la lista (index) pero lo elimina del objecto (lista)
lista = list("roberto")
removed_char = lista.pop(0)
print(f"removed letter: {removed_char}")
#removed letter: r

print(f"modified list: {lista}")
# modified list: ['o', 'b', 'e', 'r', 't', 'o']
# %%
# clear(): Elimnar todos los elementos de una lista y quedarnos con una empty list
lista = list(range(3))
lista.clear()
lista
# []

# %%
# Comparacion de objectos (listas): element-wise
lista_1 = [1,2,3]
lista_2 = [1,2,3]
print(lista_1 == lista_2) #True

lista_1 = [1,2,3]
lista_2 = [1,2]
print(lista_1 == lista_2) #False

lista_2 <= lista_1 # True
# %%

"""
DICTIONARIES

* {}/dict()
* {llave:valor} / {k:v}
"""

dict_weather = {
    "location":"Madrid",
    "date":"2022-09-27",
    "max_temp":25,
    "min_temp":15
}

print(dict_weather)
# {'location': 'Madrid', 'date': '2022-09-27', 'max_temp': 25, 'min_temp': 15}

print(type(dict_weather))
# <class 'dict'>
# %%
# dict() -> dict(k1=v1, k2=v2)
dict_weather_2 = dict(
    location="Madrid",date="2022-09-27",max_temp=25,min_temp=15
)
print(dict_weather_2)
# {'location': 'Madrid', 'date': '2022-09-27', 'max_temp': 25, 'min_temp': 15}

print(dict_weather==dict_weather_2)
# True
# %%
# limitacion dict()
dict_3 = {"if":1,"while":2}
print(dict_3)
# {'if': 1, 'while': 2}

#dict_4 = dict(if=1,while=2)
# SyntaxError: invalid syntax
# %%
# casting -> dict()
# tener en cuenta que los diccionarios necesitan de pares de valores
#dict([1,2,3,4])
# TypeError: cannot convert dictionary update sequence element #0 to a sequence

mi_lista = [ 
    ["name","roberto"],
    ["edad",38]
]
dict(mi_lista)
# {'name': 'roberto', 'edad': 38}
dict((("name","roberto"),("edad",38)))
# {'name': 'roberto', 'edad': 38}
# %%
# Modificar diccionarios / Añadir-eliminar elementos
cientificos = {}
cientificos["Albert"] = "Einstein"
cientificos["Isaac"] = "Newton"

print(cientificos)
# {'Albert': 'Einstein', 'Isaac': 'Newton'}
print(len(cientificos))
# 2

cientificos["Marie"] = "Curie"
print(cientificos)
# {'Albert': 'Einstein', 'Isaac': 'Newton', 'Marie': 'Curie'}

cientificos["Charles"] = "Darwi"
cientificos["Charles"] = "Darwin"
# {'Albert': 'Einstein', 'Isaac': 'Newton', 'Marie': 'Curie', 'Charles': 'Darwin'}
# %%
# Obtener un elemento de un diccionario: llave o get
cientificos["Albert"]
# 'Einstein'

print(cientificos.get("Albert"))
# Einstein

cientificos["Roberto"]
# KeyError: 'Roberto'

r = cientificos.get("Roberto")
print(type(r))
# <class 'NoneType'>

# Como obtener las llaves y valores de un diccionario
# keys(), values(), items()
print(cientificos.keys())
# dict_keys(['Albert', 'Isaac', 'Marie', 'Charles'])

llaves_dict = list(cientificos.keys())
print(llaves_dict)
# ['Albert', 'Isaac', 'Marie', 'Charles']

values_dict = list(cientificos.values())
print(values_dict)
#['Einstein', 'Newton', 'Curie', 'Darwin']
 
# %%

# items() -> extrae tuplas de llaves,valores
dict_weather = {
    "location":"Madrid",
    "date":"2022-09-27",
    "max_temp":25,
    "min_temp":15
}

for k,v in dict_weather.items():
    print(f"Key: {k}, Value: {v}")
# Key: location, Value: Madrid
# Key: date, Value: 2022-09-27
# Key: max_temp, Value: 25
# Key: min_temp, Value: 15
# %%
dict_weather = {
    "location":"Madrid",
    "date":"2022-09-27",
    "max_temp":25,
    "min_temp":15
}

del dict_weather["min_temp"]
print(dict_weather)
# {'location': 'Madrid', 'date': '2022-09-27', 'max_temp': 25}

# pop() -> get + del
dict_weather = {
    "location":"Madrid",
    "date":"2022-09-27",
    "max_temp":25,
    "min_temp":15
}

selected_value = dict_weather.pop("location")
print(selected_value)
# Madrid
print(dict_weather)
# {'date': '2022-09-27', 'max_temp': 25, 'min_temp': 15}
# %%
# Combinar diccionarios: **, update
dict_weather_1 = {
    "location":"Madrid",
    "date":"2022-09-27",
}

dict_weather_2 = {
    "max_temp":25,
    "min_temp":15
}

combined_dict = {**dict_weather_1, **dict_weather_2}
print(combined_dict)
#{'location': 'Madrid', 'date': '2022-09-27', 'max_temp': 25, 'min_temp': 15}
# %%
# Combinar diccionarios: **, update
dict_weather_1 = {
    "location":"Madrid",
    "date":"2022-09-27",
}

dict_weather_2 = {
    "max_temp":25,
    "min_temp":15
}

dict_weather_1.update(dict_weather_2) 
print(dict_weather_1)
# {'location': 'Madrid', 'date': '2022-09-27', 'max_temp': 25, 'min_temp': 15}
# %%
"""
TUPLES
"""
# Creating tuple () , 
tuple_names = ("Roberto", "Joaquin", "Fernando")
print(type(tuple_names))
print(tuple_names)
#<class 'tuple'>
#('Roberto', 'Joaquin', 'Fernando')

tuple_names = "Roberto", "Joaquin", "Fernando"
print(type(tuple_names))
print(tuple_names)
#<class 'tuple'>
#('Roberto', 'Joaquin', 'Fernando')
# %%
# Acceder a elementos
tuple_names[0]
# Roberto

tuple_names[:2]
# ('Roberto', 'Joaquin')

tuple_names[0] = "roberto"
#TypeError: 'tuple' object does not support item assignment

# %%
"""
SETs {}, set()
"""

my_set = {1,2,3,4}
my_set_2 = set([1,2,3,4,5,5,5,5,7])

print(my_set)
print(my_set_2)
#{1, 2, 3, 4}
#{1, 2, 3, 4, 5, 7}

set({"a":1,"b":2})
# {'a', 'b'}

# %%
# Los sets no son indexables
my_set_2[0]
# TypeError: 'set' object is not subscriptable

my_set + my_set_2
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

# %% 
# Operaciones entre sets: & (intersection), | (union), - (difference)
sets_1 = {1,2,3,4,5}
sets_2 = {4,5,6,7,8}

print(sets_1 & sets_2)
# {4, 5}
print(sets_1 | sets_2)
# {1, 2, 3, 4, 5, 6, 7, 8}

print(sets_1-sets_2)
# {1, 2, 3}

# %%
