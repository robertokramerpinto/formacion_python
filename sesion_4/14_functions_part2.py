"""FUNCTIONES - CONTINUACION
"""

# NESTED FUNCTION

# %%
from platform import python_branch


city = "Madrid"
def print_city(city_name):

    def clean_text(text):
        return str(text).strip().lower()
    
    print(clean_text(city_name))

print_city(city_name=city)
# madrid

#clean_text("Roberto")
# NameError: name 'clean_text' is not defined
# %%

def clean_text(text):
        return str(text).strip().lower()

def print_city(city_name):
    print(clean_text(city_name))

print_city("Madrid")
#madrid

clean_text("Roberto")
'roberto'
# %%

## SCOPE - Ambito de las funciones
city = "Madrid"

def print_city():
    city = "Barcelona"
    print(f"city en el ambito local: {city}")

print_city()
# city en el ambito local: Barcelona
print(f"city en el ambito global: {city}")
# city en el ambito global: Madrid
# %%
## SCOPE - Ambito de las funciones
city = "Madrid"

def print_city():
    #city = "Barcelona"
    print(f"city en el ambito local: {city}")

print_city()
# city en el ambito local: Madrid
print(f"city en el ambito global: {city}")
# city en el ambito global: Madrid
# %%
# %%
## SCOPE - Ambito de las funciones
city = "Madrid"
def print_city():
    # Utilizamos keyword global
    global city
    print(f"city en el ambito global: {city}")
    city = "Barcelona"
    print(f"city en el ambito local: {city}")

print_city()
city
# %%
"""
FUNCIONES ANONIMAS - LAMBDA FUNCTION
f = lambda x: print(x)
"""
f = lambda x: print(x)
f("Esto es una lambda function")
# Esto es una lambda function

f = lambda x: print(str(x).lower())
f("Esto es UNA lambda function")
# esto es una lambda function
# %%
lambda_suma = lambda x,y: x+y
lambda_suma(10,20) # 30
# %%

"""
ARGS & KWARGS

- *args
- **kwargs
"""
def receive_args(*args):
    for element in args:
        print(element)

receive_args("a","b","c","d")
#a
#b
#c
#d

receive_args("a","b","c","d",1,2,3)
# a
# b
# c
# d
# 1
# 2
# 3

# %%
def order_icecream(size, flavour, *toppings):
    print(f"Order: Size {size} / Flavour {flavour}")
    if len(toppings) >0:
        print("Toppings:")
        for e in toppings:
            print(e)

order_icecream(size="small",flavour="chocolate")
#Order: Size small / Flavour chocolate

order_icecream("small","chocolate","peanuts","cherry")
#Order: Size small / Flavour chocolate
#Toppings:
#peanuts
#cherry
# %%
# kwargs **
def print_keyword_args(**kwargs):
    for k,v in kwargs.items():
        print(f"Key: {k} / Value: {v}")

print_keyword_args(nome="Roberto",edad=38)
#Key: nome / Value: Roberto
#Key: edad / Value: 38
# %%
