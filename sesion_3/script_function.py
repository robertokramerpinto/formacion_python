# EXAMPLE 1 - function hello world

# # Paso 1 - definir la funcion
# def print_hello_world():
#     print("Hello World")

# # Paso 2 - llamar a la funcion
# print_hello_world()

############################################################
# EXAMPLE 2 - simple return statement
def return_input(x):
    print("Ejecutando la funcion return_input")
    return x

user_input = input("Enter any value:")
a = return_input(user_input)
print(a)