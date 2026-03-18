import requests
import pickle

# irisdata = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# file=open("irisdata.txt", "a")
# file.write(irisdata.text)
# file.close()

# file=open("irisdata.txt", "r")

# irislist=[]
# while True:
#     line=file.readline().strip()
#     if(line==""):
#         break
#     irislist.append(line)
# file.close()


# iristlistproper=[]
# for items in irislist:
#     j=0
#     templist=[]
#     for i in range(len(items)):
#         if(items[i]==","):
#             # print(items[i])
#             templist.append(items[j:i])
#             j=i+1
#     templist.append(items[j:len(items)])
#     iristlistproper.append(templist)
    

# # print(iristlistproper)


# pickleirisfile="iris data.pkl"
# pickleirisopen=open("iris data.pkl", "wb")
# pickle.dump(iristlistproper, pickleirisopen)

pickleload=open("iris data.pkl", "rb")
picklelist=pickle.load(pickleload)

for i in range(len(picklelist)):
    for j in range(len(picklelist[i])):
        print(picklelist[i][j], end="  ")
    print()


# print(irisdata.text)
