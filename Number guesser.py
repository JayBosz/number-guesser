import random

limite = input("Please select the maximum value number ")

if limite.isdigit():
    limite = int(limite)

    if limite <= 0:
        print("please choose a number that is bigger than 0 \n")
        quit()
else:
    print("Please enter a valid number next time ")
    quit()

Random_number = random.randint(0,limite)

attempts = 0

while True:
    attempts += 1
    guess = input(f"Please Guess a number between 0 and {limite} and you have 3 guesses \n")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please choose a number next time")
        continue
    if attempts == 3:
        print("Sorry, You're out of guesses")
        break

    if int(guess) == Random_number:
        print(f"You guessed right! good job, the right number is {guess} and you got it in {attempts} guesses")
        break
    elif int(guess) > Random_number:
        print(f"Too high, guess lower, you have {3-attempts} guesses left \n")
        continue
    else:
        print(f"Too low, guess higher, you have {3-attempts} guesses left \n")
        continue