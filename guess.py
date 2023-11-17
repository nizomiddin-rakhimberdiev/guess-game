import random

n = random.randint(1,10)

x = 0

while True:
    guess = int(input("1 dan 10 gacha son kiriting: "))
    if n == guess:
        print("Well done 👍")
        break
    
    x += 1

    if x == 3:
        print("Yutqazgizgiz ☹️:")
        break
    
