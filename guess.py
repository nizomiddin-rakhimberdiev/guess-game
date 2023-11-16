import random

n = random.randint(1,10)

while True:
    guess = int(input("1 dan 10 gacha son kiriting: "))
    if n == guess:
        print("Well done 👍")
        break
