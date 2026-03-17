import time
import datetime
import pygame

# 20 min water
# 30 min eye
# 45 min exercise
# all the things will stack too if not completed

def musicplay(file, stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    
    print("Type in " + stopper + " to stop the music")
    while True:
        dum=str(input())
        if(dum==stopper):
            pygame.mixer.music.stop()
            break
        else:
            print("Dude, it's just "+ stopper + " ! Try Again!")

def log_that(activity):
    f=open("health.txt", "a")
    f.write("[ " + str(datetime.datetime.now()) + " ]" + activity + "\n")


# starttime=int(time.time())
watertime=int(time.time())
eyetime=int(time.time())
exertime=int(time.time())
while True:
    totaltime=time.ctime()
    clocktime=totaltime[11:19]
    hour=int(clocktime[0:2])
    if(hour<0 or hour>17):
        break

    presenttime=int(time.time())
    if (presenttime-watertime) > 20:
        musicplay("water.mp3", "drank")
        log_that("Drank Water!")
        presenttime=int(time.time())
        watertime+=20

    if(presenttime-eyetime) > 30:
        musicplay("eye of the tiger.mp3", "eye")
        log_that("Done eye exercise")
        presenttime=int(time.time())
        eyetime+=30

    if(presenttime-exertime) > 45:
        musicplay("run it up.mp3", "exercise")
        log_that("Done physical exercise")
        presenttime=int(time.time())
        exertime+=45
    

    


















# minute_og=int(clocktime[3:5])
# second_og=int(clocktime[6:8])
# print(clocktime)
# print(hour)
# print(minute_og)
# time.sleep(2)
# print(second_og)

# for i in range(10):
#     print(time.time())
#     time.sleep(1)

# pygame.mixer.init() 
# pygame.mixer.music.load("run it up.mp3")
# pygame.mixer.music.play() # Loop forever

# Keep the program running while music plays
#while pygame.mixer.music.get_busy():
#    pygame.time.Clock().tick(10)

# print("does it work?")
# x=int(input())
# pygame.mixer.init() 
# pygame.mixer.music.load("eye of the tiger.mp3")
# pygame.mixer.music.play(-1)
# # pygame.mixer.pause()
# y=int(input())

# def musicplay(file):
#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play(-1)


# totaltime=time.ctime()
# clocktime=totaltime[11:19]
# hour=int(clocktime[0:2])

# print("[ " + str(datetime.datetime.now()))

# time_og=int(time.time())
# print(time_og)
# time.sleep(1)

# while(hour>9 and hour<22):
#     totaltime=time.ctime()
#     clocktime=totaltime[11:19]
#     hour=int(clocktime[0:2])
    
#     time_now=int(time.time())

#     if((time_now-time_og)%20==0): # minute_og-minute
#         # pygame.mixer.init()
#         # pygame.mixer.music.load("water.mp3")
#         # pygame.mixer.music.play(-1)

#         musicplay("water.mp3")

#         dum=str(input("Type 'drank' to exit: "))
#         while(dum!="drank"):
#             print("That's incorrect. Type 'drank!'")
#             dum=str(input("Now? "))
#         f=open("Health.txt", "a")
#         f.write("[ " + str(datetime.datetime.now()) + " ] " + dum + "\n")
#         f.close()
#         pygame.mixer.music.stop()
    

#     if((time_now-time_og)%30==0):
#         # pygame.mixer.init()
#         # pygame.mixer.music.load("eye of the tiger.mp3")
#         # pygame.mixer.music.play(-1)

#         musicplay("eye of the tiger.mp3")
#         dum=str(input("Type 'eye' to stop: "))
#         while(dum!="eye"):
#             print("No no no! Type 'eye' dude!")
#             dum=str(input("Now? "))
#         f=open("Health.txt", "a")
#         f.write("[ " + str(datetime.datetime.now()) + " ] " + dum + "\n")
#         f.close()
#         pygame.mixer.music.stop()

#     if((time_now-time_og)%45==0):
#         # pygame.mixer.init()
#         # pygame.mixer.music.load("run it up.mp3")
#         # pygame.mixer.music.play()

#         musicplay("run it up.mp3")
#         dum=str(input("Type 'exercise' to stop: "))
#         while(dum!="exercise"):
#             print("Bro, actually, its 'exercise'")
#             dum=str(input("Now? "))
#         f=open("Health.txt", "a")
#         f.write("[ " + str(datetime.datetime.now()) + " ] " + dum + "\n")
#         f.close()
#         pygame.mixer.music.stop()

    