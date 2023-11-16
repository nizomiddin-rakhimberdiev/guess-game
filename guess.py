import random

n = random.randint(1,10)
guess = int(input("Enter the number between 1 and 10: "))

if n == guess:
    print("Well done")
else:
    print("Wrong!")
