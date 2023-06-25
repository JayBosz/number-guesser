import random

limite = input("Please select the maximum value number")

if limite.isdigit():
    limite = int(limite)

    if limite <= 0:
        print("please choose a number that is bigger than 0")
        quit()
else:
    print("Please enter a valid number next time")
    quit()

