import os
import time

# folder dir, #text file, #.jpg

folder=str(input("Which folder(its path) do you wanna Prettify:"))
excfile=str(input("File contaning names you dont' want to change: "))
format=str(input("Files end format you want to number: "))

os.chdir(folder)

exclist = []
f=open(excfile)
while True:
    line=f.readline().strip()
    # line.strip()
    if(line==""):
        break
    exclist.append(line)
    # print(exclist)
    # time.sleep(2)

# print(exclist)
f.close()

files=os.listdir()
j=1
count=0
for i in range(len(files)):
    for k in range(len(exclist)):
        if(os.path.splitext(files[i])[0]==exclist[k]):
            count+=1
            continue
    if(count==1):
        count=0
        continue
    if(os.path.splitext(files[i])[1]==format):
        os.rename(files[i], str(j) + format)
        j+=1
        continue

    capital=files[i].capitalize()
    # print(capital + " " + x)
    os.rename(files[i], capital)

# print(files)