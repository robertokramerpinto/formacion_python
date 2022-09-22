""" BUCLES

WHILE / FOR

# WHILE

while <condition>:
    execute 1
    execute 2
"""
# %%
if True:
    print("Onte time print")
# %%
while True:
    print("Please kill me :) ")

# %%
count = 1
while count <= 5:
    count += 1
    print(count)
print("End Loop")
# %%
import random
number = random.randint(1,10)

number_of_guesses = 0
control = True
while control:
    guess = int(input("Guess a number from 1 to 10:"))
    number_of_guesses += 1
    if number == guess:
        print("Congrats!! Number: ",guess)
        control = False
# %%
""" FOR
* iteracion sobre elementos de una coleccion de datos
* evalua una determinada condiccion para cada elemento en este conjunto
* lists, tuples, str

for value in sequence:
    [do something]

"""
lista_numbers = [1,2,3,4,5]
for number in lista_numbers:
    print(number)
# %%
lista_numbers = [1,2,3,4,5]
for number in lista_numbers:
    print(number)

# %%
for n in [1,2,3,4,5]:
    print(n)

# %%
word = "barcelona"
for letter in word:
    print(letter)


"""
WHILE - BREAK, CONTINUE

break: nos permite salir de un loop siempre que una condicion se cumple
continue: mas utilizado con una condicion if. Si tenemos un continue nos hace retornar al nivel inicial del loop
"""
# %%
count = 1
while count <= 5:
    if count == 3:
        break
    print(count)
    count += 1
print("END WHILE")
# %%
# Example - while and continue
count = 1
while count <= 10:
    if count == 8:
        break
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
print("END WHILE")
# %%

"""
FOR - BREAK, CONTINUE
"""
nombre = "roberto"
for letter in nombre:
    if letter.lower() == "e":
        break
    print(letter)
print("End FOR Loop") 
# %%
for number in range(10):
    if number == 5:
        continue
    print(number)
print("End FOR Loop")
# %%
