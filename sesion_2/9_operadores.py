"""
Operadores 
* Operadores aritmeticos
* Operadores logicos
* Operadores relacionales

######  Operadores aritmeticos
* operaciones con los numeros

'+' : adicion de valores
'-' : subtracción de valores
'*' : multiplicación 
'/' : división

'%' : modulo de los valores
'**': potencia
'//': division resultado entero
"""

#%%
print(7%3)
# 1
print(9%3)
# 0

print(2**3)
#8

print(7//2)
#3
# %%
a = 12
b = 4
print(a//b)
3
# %%
nombre = "roberto"
apellido = "kramer"
print(nombre+apellido)
# robertokramer
# %%
############ Operadores de asignacion + aritmeticos
a = 1
a = a + 1
print(a)
# 2

a = 1
a += 1 # -> a = a + 1
print(a)
# 2 
# %%
############################ Operadores Relacionales
# Comparación entre objectos -> retornan un bool (True/False)
# == Equal
# != Not Equal 
# >, >= , <, <= 

print('a'=='b')
# False

print(1 == True)
# True

print(0 != False)
# False

print(1_000 > 10_000)
# False

print("abc" > "zwdc")
# False
# %%
########### Operadores Logicos
# Retornan un valor bool (True/False)
# Los inputs tambien tienen que ser bool
# and: retorna True si los 2 valores son True
# or: retorna True si uno de los valores es True
# not : reverso del resultado

# Tabla AND
print(True and True) # True
print(True and False) #False
print(False and True) #False
print(False and False) #False
# %%
# Tabla OR 
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False
# %%
print(not True) # False
print(not False) # True
print(not 1) # False
# %%
cond_1 = 1 > 2
cond_2 = 10 > 5
print(cond_1 and cond_2) #False
print(cond_1 or cond_2) #True
# %%
# is / not is: retornar bool (is -> True si variables/valores son los mismos objectos)
# in / not in: retornar bool (in -> True si un elemento es parte de un conjunto de elementos)

list_nombres = ["roberto","joaquin","marcelo"]
print("Roberto" in list_nombres) #False
print("Roberto" not in list_nombres) #True
print("joaquin" in list_nombres) #True
# %%
a = 1
print(a is True) #False
print(a == True) #True
# %%
