import random
print("Welcome!Let's begin the game")
n=random.randint(1,10)
print("You have 4 Guesses.You can begin Guessing now")
count=0
while count!=4:
    a=int(input(f"Enter your guess number {count+1}\n"))
    if a==n:
        print("Yay!You have won")
        break

    else:
        print("Try again")
    count+=1
if count==4:
    print("Sorry!You have lost")
