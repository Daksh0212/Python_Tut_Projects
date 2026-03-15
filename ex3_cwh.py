import random

n=random.randint(1, 1000)
guess=8

while(guess!=0):
    x=int(input("Please Enter your number: "))
    if(x>n):
        print("Go lower bub")
    elif(x<n):
        print("you can go a little higher")
    elif(x==n):
        break
    guess-=1
    print("You have ", guess, " guesses left\n")


if(guess>0):
    print("You Won!, You took like: ", 8-guess, " guesses")
elif(guess<=0):
    print("Sorry you lost :p")

