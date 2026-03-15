n=int(input("Enter the number: "))
boolean=int(input("1 or 0 ? "))

boolean=bool(boolean)

if(boolean==True):
    for i in range(1, n+1):
        # print("*"*i)
        for j in range(1, i+1):
            print("*", end="")
        print()
elif(boolean==False):
    for i in range(n, 0, -1):
        print("*"*i)