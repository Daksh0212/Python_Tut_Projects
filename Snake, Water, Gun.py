import random

game={"s":"snake", "w":"water", "g":"gun"}
game_comp=["s", "w", 'g']
userpts, comppts = 0, 0

i=1
while(i<11):
    print("\nWe are at ", i, "th round")
    comp=random.choice(game_comp)
    user=str(input("s(snake), w(water), g)gun, choose! "))

    if(user==comp):
        print("Game Drawn")
    elif((user=="s" and comp=="w") or (user=="w" and comp=="g") or (user=="g" and comp=="s")):
        print("You Won This!")
        userpts+=1
    elif((user=="s" and comp=="g") or (user=="w" and comp=="s") or (user=="g" and comp=="w")):
        print("You Lose this one!")
        comppts+=1
    else:
        print("Dude, atleast give some correct Input. Try Again!")
        continue

    print("Your choice is: ", game[user], " and computer's choice is: ", game[comp])

    print("Your Points: ", userpts, "  Computer points: ", comppts)
    i+=1

if(userpts>comppts):
    print("\nYou Won the Entire Game!\nYour Points are ", userpts, " and computer Points are ", comppts)
elif(comppts>userpts):
    print("\nYou Lost this Game!\nYour Points are ", userpts, " and computer Points are ", comppts)
else:
    print("\nThe Game is a final draw!\nYour Points are ", userpts, " and computer Points are ", comppts)