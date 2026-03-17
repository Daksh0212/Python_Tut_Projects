from win32com.client import Dispatch
# import json
import requests
import datetime

def speak(str):
    speak=Dispatch("SAPI.SpVoice")
    speak.Rate=2
    speak.Speak(str)

def printAndSpeakNews(data, index):
    print("\n\n\nNumber " + str(index+1))
    print("\nThe Source is: " + data["articles"][index]["source"]["name"])
    print("\nThe Article states:\n" + data["articles"][index]["title"])
    print("\nThe Description says:\n" + data["articles"][index]["description"])

    speak("\n\n\nNumber " + str(index+1))
    speak("The Source is: " + data["articles"][index]["source"]["name"])
    speak("The Article states:\n" + data["articles"][index]["title"])
    speak("\nThe Description says:\n" + data["articles"][index]["description"])


print("\nHey there, Welcome to the News API, Lets customize your feed first\n")
amount=str(input("So how many news do you want to hear (default 5): "))
q=str(input("Any particular keyword you're interested in? (default India): "))
category=str(input("Any particular category you're interested in? (can leave blank): "))
domain=str(input("Any particular news channel you're interested in? (please provide its ID): "))
timenews=str(input("Of how many days do you want to see news of: (default is 0(today)): "))
if(amount==""):
    amount=5
if(timenews==""):
    timenews="0"
if(q==""):
    q="India"
amount=int(amount)
timenews=int(timenews)
print("\nOk cool. Here is the top news served straight to you along with our voice buddy!\n\n")

todate=str(datetime.date.today())
fromdate=str(datetime.date.today()-datetime.timedelta(days=timenews))
# print(fromdate)

response = requests.get("https://newsapi.org/v2/everything?" + "q=" + q + "&category=" + category + 
                        "&domain=" + domain + "&from=" + fromdate + "$to" + todate + "&sortBy=popularity&apiKey=fa3b14066199404ca05f995f025ee40c")

data = response.json()
# print(data)

for i in range(amount):
    printAndSpeakNews(data, i)

print("\n\n\nThank You for Today. Come back again for more of these amazing news!\n\n")
speak("\n\n\nThank You for Today. Come back again for more of these amazing news!\n\n")