# BUILT-IN FUNCTION

#%%
# Map
# aplica una determinada funcion a todos los elementos de una secuencia (lista)
# syntax: map(function,iterable)
# retorna: un iterator que puede ser convertido a una lista, tupla, etc.
def clean_text(text:str)->str:
    """Cleans the input text by applying the following steps:
    - strip
    - lowercase

    Parameters
    ----------
    text : str

    Returns
    -------
    str
    """
    clean_str = str(text).strip().lower()
    return clean_str

raw_text = "  RoberTO   "
clean_text(raw_text)
# roberto

raw_text = [
    " Hello, my name is Roberto ", 
    " I'm from BrAZiL  ",
    " I livE in MadrID ",
]

treated_text = map(clean_text, raw_text)
print(treated_text)
# <map object at 0x112c7c460>

treated_text = list(map(clean_text, raw_text))
print(treated_text)
#['hello, my name is roberto', "i'm from brazil", 'i live in madrid']
# %%
numbers = [1,2,3,4,5]
squared_numbers = list(
    map(lambda x: x**2, numbers)
)
squared_numbers
#[1, 4, 9, 16, 25]
# %%
# Filter
# filter() extrae elementos de una coleccion (lista, tupla)
# para los cuales una funcion retorna True
# syntax: filter(function, iterable)

def is_greater_than_10(x):
    if x > 10:
        return True
    else:
        return False

numbers = list(range(15))
filtered_numbers = list(filter(
    is_greater_than_10,numbers
))
filtered_numbers
# [11, 12, 13, 14]
# %%
# Reduce
# reduce() -> aplica una funcion a un iterable de manera secuencial a sus elementos
# syntax: reduce(function,iterable)
# retorna un unico valor
# la funcion reduce() se importa a traves de functools

import functools
numbers = [1,2,3,4,5]
f_lambda_suma = lambda x,y: x+y

reduced_result = functools.reduce(
    f_lambda_suma, numbers
)
print(reduced_result)
# 15
# %%
# ZIP
# zip() -> toma colecciones retorna una lista de tuplas como resultado de la agregacion de los iterables
# syntax: zip(iterable1,iterable2, ...)

cities = ["Madrid","Barcelona","London"]
postal_codes = [28000,00000,11111]
items = zip(cities, postal_codes)
print(items)
#<zip object at 0x1104baa40>

items = list(zip(cities, postal_codes))
print(items)
# [('Madrid', 28000), ('Barcelona', 0), ('London', 11111)]
# %%
cities = ["Madrid","Barcelona","London"]
postal_codes = [28000,00000,11111]
items = zip(cities, postal_codes)
print(items)
#<zip object at 0x1104baa40>

items = list(zip(cities, postal_codes))
print(items)
# [('Madrid', 28000), ('Barcelona', 0), ('London', 11111)]

# %%
cities = ["Madrid","Barcelona","London"]
postal_codes = [28000,00000,11111]
names = ["a","b","c"]
items = list(zip(cities, postal_codes,names))
print(items)
#[
# ('Madrid', 28000, 'a'), 
# ('Barcelona', 0, 'b'), 
# ('London', 11111, 'c')
# ]
# %%
cities = ["Madrid","Barcelona","London"]
postal_codes = [28000,00000,11111]
names = ["a","b"]
items = list(zip(cities, postal_codes,names))
print(items)
#[('Madrid', 28000, 'a'), ('Barcelona', 0, 'b')]

# %%
# all/any
# all: retorna True si todos los elementos en una secuencia son True
# any: retorna True si al menos 1 elemento en una secuencia es True

all([True,True,1]) #True
all([True,True,0]) #False

any([False,False,False,0]) #False
any([True,False,False,0]) #True

# %%
text = ["A","b","C","d"]
all(map(lambda x: x.islower() == True,text)) #False

text = ["A","b","C","d"]
any(map(lambda x: x.islower() == True,text)) #True

text = ["a","b","c","d"]
all(map(lambda x: x.islower() == True,text)) #True

# %% 
# ROUND, POW
# round -> rounds a float number
# syntax -> round(number, n_decimals)

# pow -> calcula la exponenciacion de 2 numeros, utilizando como base el 1
# syntax pow -> pow(n1, n2)

print(round(1.223232)) #1
print(round(1.223232,4)) #1.2232

pow(2,3) # 8
pow(3,2) # 9

# %%
# sum()
# max(), min()

sum([1,10,20]) #31
sum(["r","a","b"])
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

numbers = [1,2,90,15,-5]
min_value = min(numbers)
max_value = max(numbers)
print(f"Min value:{min_value} / Max value:{max_value}")
# Min value:-5 / Max value:90

# %%
# Sorted
# sorted() -> ordena los elementos de una coleccions (asc or desc)
# syntax: sorted(iterable, reverse=True/False)

numbers = [1,2,90,15,-5]
print(sorted(numbers))
#[-5, 1, 2, 15, 90]

print(sorted(numbers,reverse=True))
# [90, 15, 2, 1, -5]
# %%
