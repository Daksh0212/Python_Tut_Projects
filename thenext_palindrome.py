def palindrome(n):
    k=0
    while(n!=0):
        k=k*10+n%10
        n=n//10
    return k

size=int(input("size: "))
l1=[]
for i in range(size):
    dum=int(input("Number " + str(i+1) + " : "))
    l1.append(dum)

palinlist=[]
for num in l1:
    while(num!=palindrome(num)):
        # print(num)
        num+=1
    palinlist.append(num)

for i in range(int(len(palinlist))):
    print(str(l1[i]) + " will go till: " + str(palinlist[i]) + " to get the palindrome")

    