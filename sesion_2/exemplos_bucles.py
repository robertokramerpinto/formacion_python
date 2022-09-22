import random
number = random.randint(1,10)

number_of_guesses = 0
control = True
while control:
    if number_of_guesses >= 4:
        print("Sorry. Next time")
        break
    guess = int(input("Guess a number from 1 to 10:"))
    number_of_guesses += 1

    if (number == guess):
        print("Congrats!! Number: ",guess)
        control = False
print("Game Over !!")

# number = int(input("Enter a number from 1 to 10:"))
# suma = 0
# for n in range(number+1):
#     if n % 2 == 0:
#         suma += n
# print("Total suma:", suma)
# print("End FOR")
