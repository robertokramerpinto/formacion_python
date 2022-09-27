# TRABAJANDO CON LAS CADENAS DE TEXTO

# REVIEW
# Concatenacion 
# obtener una substring 
# Funciones/metodos

"""
REVIEW
"""
# %%
# Ejemplo - creando strings : str(), '', "", """ """"
string_1 = 'string_1'
string_2 = "string_2"
string_3 = """
string_3
"""
for text in [string_1, string_2, string_3]:
    print(text)
    print(type(text))
# string_1
# <class 'str'>
# string_2
# <class 'str'>

# string_3

# <class 'str'>
# %%
# str() -> casting
str(1)
str(1.0)
str(1==1.)
str({"name":"roberto"})
str([1,2,3])
# %%
# Ejemplos - Escape (\)
# \n
print("Roberto\nKramer")
# Roberto
# Kramer

# Tab -> \t
print("Roberto\tKramer\tPinto")
# Roberto	Kramer	Pinto

texto = "'Roberto' said him."
print(texto)
# 'Roberto' said him.
print("\"Roberto\" said him.")
#"Roberto" said him.
# %%
"""
CONCATENACION DE STRINGS
"""

# %%
# EXAMPLE : +
print("Mi" + "Nombre" + "es" + "ROBERTO")
#MiNombreesROBERTO

print("Mi" + " " + "Nombre" + " " + "es" + " " + "ROBERTO")
#Mi Nombre es ROBERTO

number1 = str(1)
number2 = str(.5)
number3 = number1+number2
print(number3)
# 10.5
# %%
# Ejemplo - multiplicar strings *
print("*" * 5)
# *****

print("hello" * 5)
# hellohellohellohellohello

# %%
"""
FORMATACION - FORMATTING

* Old style (python2 y python3) -> % 
* New style (python > 3.6) -> f-strings (best practice)

"""
# %% 
# Old Style (%)
# %s: strings
# %d: decimal integer
# %f: decimal float

username = "Joaquin"
msg = "Your name is %s" % username
print(msg)
# Your name is Joaquin

username = "Roberto"
age = 38
msg = "Your name is %s and your age is %d" % (username,age)
print(msg)
# Your name is Roberto and your age is 38

msg = "Your name is %s and your age is %s" % (age,username)
print(msg)
#Your name is 38 and your age is Roberto
# %%
# Formatting floats
number = 10/3
print(number)
# 3.3333333333333335

print("%f" % number)
# 3.333333
print("%.2f" % number)
# 3.33
print("%.4f" % number)
# 3.3333

# %%
# f-string Formatting (new style > 3.6python)
# f" {} "

username = "Roberto"
msg = f"Your name is {username}"
print(msg)
# Your name is Roberto
# %%
# f-string multiple variables
username = "Roberto"
age = 38
msg = f"Your name is {username} and your age is {age}"
print(msg)
# Your name is Roberto and your age is 38
# %%
name = "Roberto"
age = 38
f'{name} and {age}'
# 'Roberto and 38'

f"""{name}"""
'Roberto'

# %%
# f-string - Formatting float {var:.3f}
float_number = 10/6
print(float_number)
#1.6666666666666667

print(f"{float_number:.3f}")
# 1.667
# %%

"""
SUBSTRINGS - OBTENCION PARCIAL DE UNA CADENA DE TEXT
"""

# %%
# OBTENER 1 char dentro de la string: []
text = "abcdefghij"
print(f"{text[0]}: 1st letter")
# a: 1st letter

text[3]
# 'd'
text[-1]
# 'j'
text[-2]
'i'

# a b c d e f
# 0 1 2 3 4 5
# -6 -5 -4 - 3 -2 -1
# %%
for a in text[0:3]:
#for a in range(3):
    print(a)
# a
# b
# c

# %%
# Example - slicing [start:end:step]
# [:] -> [0:-1] -> toda la secuencia
# [start:] -> [start:-1]
# [:end] -> [0:end]
# [::-1] -> inverse
texto = "abcdefghij"

print(texto[:]) # abcdefghij
print(texto[2:]) # cdefghij
print(texto[:-2]) # abcdefgh

# a b c d e f g h i j
# 0 1 2 3 4 5 6 7 8 9
print(texto[1:-1:2])
#bdfh
print(texto[::-1])
#jihgfedcba
# %%

"""
FUNCIONES Y METODOS
"""
# lenght len()
texto = "abcdefghij"
length = len(texto)
print(f"Length: {length}")
#Length: 10
# %%

# split() -> metodo strings -> retorna una lista de substrings de acuerdo con un separador de texto
numbers_text = "1,2,3,4,5,6"
print(type(numbers_text))
print(numbers_text)

split_text = numbers_text.split(",")
print(split_text)
#['1', '2', '3', '4', '5', '6']
print(type(split_text))
# <class 'list'>
# %%
# split() -> utiliza el whitespace como sep por defecto
numbers_text = "1,2,3,4,5,6"
split_text = numbers_text.split()
print(split_text)
# ['1,2,3,4,5,6']
print(type(split_text))
# <class 'list'>
len(split_text) #1

text = "My name is Roberto!!"
print(text.split()) # ['My', 'name', 'is', 'Roberto!!']
# %%
# join() -> es un str method que junta los valores de una secuencia (lista) en una string (retorna una string)
# donde los valores tambien son separados por un sep (delimiter)
# syntax: '<sep>'.join(<sequence>)

lista_words = ["Roberto", "Kramer","Pinto"]
nombre = " ".join(lista_words)
print(nombre)
# Roberto Kramer Pinto

",".join(lista_words)
#'Roberto,Kramer,Pinto'

",".join("Hello")
'H,e,l,l,o'

":".join({"name":"Roberto", "edad":38})
'name:edad'
# %%
