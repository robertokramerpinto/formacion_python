"""
FUNCIONES
INPUTS (ENTRADA) PARAMETROS --> EJECUTAN UNA TAREA (ALGORITMO) --> OUTPUT

2 PASOS IMPORTANTES:
- DECLARAR LA FUNCION
- LLAMAR FUNCION
"""

# %%
# DECLARACION DE UNA FUNCION -> def + <nombre de la funcion>(<parametros>):
#                                   indentacion del codigo a ser ejecutado por la funcion

from readline import append_history_file


def print_hello_world():
    print("Hello World")
    print("Ola Mundo")

def print_object(s):
    print(s)

print_hello_world()
#Hello World
#Ola Mundo

# print_object()
# TypeError: print_object() missing 1 required positional argument: 's'

print_object(s=1)
# 1

print_object("roberto")
# roberto

print_object({"name":"Roberto"})
# {'name': 'Roberto'}
# %%
# RETORNO -> return
def print_hello_world():
    print("Hello World")
    print("Ola Mundo")

response = print_hello_world()
print(type(response))
print(response)
#Hello World
#Ola Mundo
#<class 'NoneType'>
#None
# %%
# Ejemplo - function + return statment
def return_input(x):
    print("Ejecutando la funcion return_input")
    return x

a = return_input("roberto")
print(a)
#Ejecutando la funcion return_input
#roberto
# %%
# Exemple - multiple parameters
def suma_numeros(a,b):
    return a+b

suma_numeros(1,2)
# 3
suma_numeros(1,True)
# 2
suma_numeros(1,"roberto")
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# %%
# Paso de argumentos por posicion, nombre del parametro
def print_full_name(nombre, apellido):
    print(f"Nombre: {nombre}, Apellido:{apellido}")

print_full_name("Roberto","Kramer")
# Nombre: Roberto, Apellido:Kramer

print_full_name("Kramer","Roberto")
#Nombre: Kramer, Apellido:Roberto

print_full_name(nombre="Roberto",apellido="Kramer")
# Nombre: Roberto, Apellido:Kramer
print_full_name(apellido="Kramer", nombre="Roberto")
# Nombre: Roberto, Apellido:Kramer
# %%
# PASO DE VALORES POR DEFECTO y OPCIONALES
def multiply_two_numbers(x,y):
    print(f"Multiplying numbers: {x} * {y}")
    return x*y

a = multiply_two_numbers(2,10)
a = multiply_two_numbers(x=2,y=10)
print(a)
# Multiplying numbers: 2 * 10
# 20

# Example - error calling function
multiply_two_numbers(1)
# TypeError: multiply_two_numbers() missing 1 required positional argument: 'y'

multiply_two_numbers()
# TypeError: multiply_two_numbers() missing 2 required positional arguments: 'x' and 'y'

multiply_two_numbers(y=1)
# TypeError: multiply_two_numbers() missing 1 required positional argument: 'x'
# %%
def multiply_two_numbers(x=1,y=1):
    print(f"Multiplying numbers: {x} * {y}")
    return x*y

multiply_two_numbers()
# Multiplying numbers: 1 * 1
# 1

def print_name(nombre):
    apellido = "AAAA"
    if apellido is None:
        print("Apellido not available")
        print(f"Nombre: {nombre}")
    else:
        print(f"Nombre: {nombre}, Apellido:{apellido}")

print_name(nombre="Roberto")
#Apellido not available
#Nombre: Roberto

print_name(nombre="Roberto",apellido="Kramer")
#Roberto, Apellido:Kramer

print_name(nombre="Roberto")
# %%
# Orden a la hora de definir/utilizar los parametros con valores por defecto
def multiply_two_numbers(x,y=1):
    print(f"Multiplying numbers: {x} * {y}")
    return x*y

multiply_two_numbers()
#TypeError: multiply_two_numbers() missing 1 required positional argument: 'x'

multiply_two_numbers(x=10)
# Multiplying numbers: 10 * 1
# 10

#def multiply_two_numbers(y=1, x):
#    print(f"Multiplying numbers: {x} * {y}")
#    return x*y
# SyntaxError: non-default argument follows default argument

def multiply_two_numbers(x,y=1):
    print(f"Multiplying numbers: {x} * {y}")
    return x*y
# %%
# DOCSTRINGS - Documentacion de las funciones
# añadir una string abajo del def statement
def multiply_two_numbers(x:int,y:int)->float:
    """Return the multiplication between x and y: x * y

    Parameters
    ----------
    x : int
        1st number to multiply
    y : int
        2nd number to multiply

    Returns
    -------
    float
        multiplication between x and y: x*y
    """

    print(f"Multiplying numbers: {x} * {y}")
    return x*y


# %%
