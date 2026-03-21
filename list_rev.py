list1=[1, 2, 4, 6, 8]

for i in range(0, (int(len(list1)/2))):
        temp=list1[i]
        list1[i]=list1[int(len(list1))-1-i]
        list1[int(len(list1))-1-i]=temp
print(list1)