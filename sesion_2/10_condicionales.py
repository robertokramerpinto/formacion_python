"""
# Condicionales

IF/ELSE
IF/ELIF/ELSE

* Nos ayudan en una toma de decisiones
"""

"""
IF

* Condicion que puede ser utilizada de manera independiente

if <condition> is True:
    <execute this piece of code>
 
"""
# %% 
name = "joaquin"
if (name == "roberto"):
    print("Usuario Reconocido:")
    print(name)
# %%
number = 10
if number > 5:
    print(number)
    print("Hello!!")
# %%
number = 10
if number > 5:
    if number <8:
        print(number)
# %%
name = "roberto"
if (name == "roberto"):
    print("Usuario Reconocido:")
print("End of Code")
#Usuario Reconocido:
#End of Code
# %%
"""
IF/ELSE

Las condiciones IF/ELSE son complementarias

if <condition> is True:
    <execute this piece of code>
else: # <condition> is False
    <execute this piece of code>

"""
number = 7
if number % 2 == 0:
    print("Par")
else:
    print("Impar")
print("End of code")
# %%
number = 3
if number < 10:
    print("Number < 10")
    if number > 5:
        print("Number < 5")
else:
    print("Number >= 10")
print("Number: ",number)

# %%
# if + and/or
city = "Mallorca"
if (city[0].lower() == "m") and (city[-1].lower() == "a"):
    print("City:",city)
else:
    print("Unknown City")
print("End of Code")

"""
 IF/ELIF/ELSE

* multiple if conditions

if <condition> is True:
    <execute this piece of code>
elif <condition> is True:
    <execute this piece of code>
elif <condition> is True:
    <execute this piece of code>
else: # all <condition> are False
    <execute this piece of code>
"""
#%%
age = 5
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 1
print("Precio billete: ",price)
print("Edad: ",age)
#Precio billete:  5
#Edad:  5

# %%
"""
Operadores Ternarios

<value1> if <condition> else <value2>
"""
number = 10
print(1 if (number>5) else 0)
# 1

number = 3
print(1 if (number>5) else 0)
# 0
# %%
