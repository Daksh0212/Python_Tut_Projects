op=str(input("Operator: "))
x=int(input("first: "))
y=int(input("second: "))

if(op=="+"):
    if(x==45 and y==3):
        print(60)
    else:
        print(x+y)
elif(op=="-"):
    print(x-y)

elif(op=="*"):
    if(x==7 and y==5):
        print(30)
    else:
        print(x*y)
elif(op=="/"):
    if(x==56 and y==6):
        print(9)
    else:
        print(x/y)
else:
    print("Invalid")