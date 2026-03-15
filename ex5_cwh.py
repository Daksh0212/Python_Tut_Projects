# lock retrieve
# harry rohan hammad
# diet exercise

def getDate():
    import datetime
    return str(datetime.datetime.now())

log=["harry"]
thing=["diet"]


lore=int(input("1 for lock, 2 for retrieve: "))
haroha=int(input("1 for harry, 2 for rohan, 3 for hammad: "))
diex=int(input("1 for diet, 2 for exercise: "))
print()



if lore==1:
    if haroha==1:
        if diex==1:
            dum=str(input("Harry Bhai ki diet: "))
            f=open(log[0] + "_" + thing[0] + ".txt", "a")
            #f.write("[ ", getDate(), " ]", " : ", dum)
            # haha lol i had to add + lol now I'm kinda screwed
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
        elif diex==2:
            dum=str(input("Harry Bhai ki exercise: "))
            f=open("harry_exercise.txt", "a")
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
    elif haroha==2:
        if diex==1:
            dum=str(input("Rohan Bhai ki diet: "))
            f=open("rohan_diet.txt", "a")
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
        elif diex==2:
            dum=str(input("Rohan bhai ki exercise: "))
            f=open("rohan_exercise.txt", "a")
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
    elif haroha==3:
        if diex==1:
            dum=str(input("Hammad Bhai ki diet: "))
            f=open("hammad_diet.txt", "a")
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
        elif diex==2:
            dum=str(input("Hammad bhai ki exercise: "))
            f=open("hammad_exercise.txt", "a")
            f.write("[ ")
            f.write(getDate())
            f.write(" ]")
            f.write(" : ")
            f.write(dum)
            f.write("\n")
            print("Successfully Written!")
            
if lore==2:
    if haroha==1:
        if diex==1:
            f=open("harry_diet.txt")
            print(f.read())
        elif diex==2:
            f=open("harry_exercise.txt")
            print(f.read())
    elif haroha==2:
        if diex==1:
            f=open("rohan_diet.txt")
            print(f.read())
        elif diex==2:
            f=open("rohan_exercise.txt")
            print(f.read())
    elif haroha==3:
        if diex==1:
            f=open("hammad_diet.txt", "a")
            print(f.read())
        elif diex==2:
            f=open("hammad_exercise.txt")
            print(f.read())