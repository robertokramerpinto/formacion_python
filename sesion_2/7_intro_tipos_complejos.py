"""
Introducion a tipos de datos complejos

* List 
* Tuple
* Sets
* Dictionary
* Range


######### List (Listas)

lista = [1,2,3]

* Son objectos utilizados para guardar una colección de datos en un orden particular
* Pueden contener distintos tipos de datos
"""

# %%
# Lista Empty
list_empty = []
print(type(list_empty))
# <class 'list'>

# %%
# Lista - integers
list_integers = [1,2,3,4,5]
print(type(list_integers))
# <class 'list'>
# %%
list_string = ["roberto","alberto"]
print(type(list_string))

list_float = [1.5,2.3]
print(type(list_float))

# <class 'list'>
# <class 'list'>
# %%
# Help 
help(list)
# %%
lista_mixed = [1, 2.5, "roberto", True]
print(type(lista_mixed))
# <class 'list'>
# %%
lista_nested = [[1,2,3],["roberto"],True, 5.12]
print(type(lista_nested))
# <class 'list'>

# Mutables
# - Cambiar de tamaño
# - Distintos tipos de datos


#%%
###################################### Tuples
tuple_empty = ()
print(type(tuple_empty))
# <class 'tuple'>
# %%
help(tuple)
# %%
# List/Tuple - 1 element
single_list = [1]
single_list
# [1]

single_tuple = (1)
print(type(single_tuple))
# <class 'int'>
# Python no acepta como tuple (x)

single_tuple = ("roberto")
print(type(single_tuple))
# <class 'str'>
# %%
# Creacion de una tupla con 1 unico elemento
single_tuple = (1,)
print(type(single_tuple))
print(single_tuple)
#<class 'tuple'>
#(1,)
# %%
tup_num = (1,2,3)
tup_num
# %%
tuple_mixed = ("roberto",1,5.123,True)
print(tuple_mixed)
print(type(tuple_mixed))
# %%
# Mutable objects
lista_num = [1,2]
tupla_num = (1,2)

tupla_num[0] = -1
# TypeError: 'tuple' object does not support item assignment
# %%
######### Diccionarios
# * Conjunto de elementos -> clave/valor {key:value}
# * No tienen un sentido de orden
# * claves unicas

# list [], tuple (), dict {}

dict_empty = {}
print(type(dict_empty))
# <class 'dict'>
# %%
help(dict)
# %%
dict_names = {
    "name":"Roberto"
}
print(dict_names)
# {'name': 'Roberto'}

print(dict_names["name"])
# Roberto
# %%
dict_2 = {"nombre":"Roberto", "age":38}
print(dict_2)
# {'nombre': 'Roberto', 'age': 38}

print(dict_2["nombre"])
print(dict_2["age"])
#Roberto
#38
# %%
dict_3 = {
    1:1,
    "1":"Roberto",
    2: [1,2,3],
    "2": {"a":"b"}
}
#print(dict_3)
#{1: 1, '1': 'Roberto', 2: [1, 2, 3], '2': {'a': 'b'}}
print(dict_3["2"])
#{'a': 'b'}
print(dict_3["2"]["a"])
# b
dict_3["2"]["a"].upper()
#'B'
# %%
dict_3.keys()
#dict_keys([1, '1', 2, '2'])
# %%
duplicated_dict = {
    "name":"roberto",
    "name":"ROBERTO"
}
print(duplicated_dict)
# {'name': 'ROBERTO'}
# %%
##### Sets
# * "llaves" de un diccionario
# * sets tambien no permiten elementos duplicados
# set {}

# list [], tuples (), dict {k:v}, sets {}

set_empty = {}
print(type(set_empty))
# <class 'dict'>
# Para crear un set vacio tenemos que utilizar set()
set_empty = set()
print(type(set_empty))
#<class 'set'>
# %%
set_1 = {1,2,3}
print(type(set_1))
# <class 'set'>
# %%
my_set = {1,1,2,3,3,4}
print(my_set)
# {1, 2, 3, 4}
# %%
my_set = {1,2,3,4,True}
print(my_set)
{1, 2, 3, 4}
# %%
######## Rangos - Ranges
# range()
# range(start, stop, step)
# -> te crea una secuencia de numeros empiezando por el start, hasta el stop (no incluyido), saltando de acuerdo con el step
range_example_1 = range(5)
#print(range_example_1)
# range(0, 5)
print(list(range_example_1))
# [0, 1, 2, 3, 4] -> range(5)
# %%
rango_2 = range(2,13,3)
print(list(rango_2))
# [2, 5, 8, 11]

rango_3 = range(2,15,3)
print(list(rango_3))
[2, 5, 8, 11, 14]
# %%

## Casting 
# conversion entre distintos tipos de datos
# int(), float(), str(), bool(), list(), tuple(), dict(), set()

# float -> str
print(type(str(1.3)))
# <class 'str'>

int("1.5")
# %%
