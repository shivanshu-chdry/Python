#Healthy Programmer
from pygame import mixer
import datetime
import time

def gettime():
    return datetime.datetime.now()

def water_alert():
    mixer.init()
    mixer.music.load('Exercise11water.mp3') 
    mixer.music.set_volume(0.2)
    mixer.music.play()

def eye_alert():
    mixer.init()
    mixer.music.load('Exercise11eye.mp3') 
    mixer.music.set_volume(0.2)
    mixer.music.play()

def physical_alert():
    mixer.init()
    mixer.music.load('Exercise11physicalexercise.mp3') 
    mixer.music.set_volume(0.2)
    mixer.music.play()



log = 8
while log>1:
    print('Welcome to Healthy Programmer!')
    water_alert()
    water_user = input('Time to drink some water! Type \'drank\' if done...\n')
    if water_user=='drank':
        mixer.music.stop()
        w= open('Exercise11waterlog.txt', 'a')
        w.write(str([str(gettime())]) + ' ' + water_user + "\n")
        w.close()
    else:
        print('Enter a valid input!')
    log = log - 1
    print(f'Logs left: {log}')
    time.sleep(1800)

    eye_alert()
    eye_user = input('Time to relax your eyes! Type \'relaxed\' if done...\n')
    if eye_user=='relaxed':
        mixer.music.stop()
        e = open('Exercise11eyelog.txt', 'a')
        e.write(str([str(gettime())]) + ' ' + eye_user + "\n")
        e.close()
    else:
        print('Enter a valid input!')
    log = log - 1
    print(f'Logs left: {log}')
    time.sleep(900)

    physical_alert()
    physical_user = input('Time to do some exercise! Type \'exercise done\' if done...\n')
    if physical_user=='exercise done':
        mixer.music.stop()
        p = open('Exercise11physicallog.txt', 'a')
        p.write(str([str(gettime())]) + ' ' + physical_user + "\n")
        p.close()
    else:
        print('Enter a valid input!')
    log = log - 1
    print(f'Logs left: {log}')
    time.sleep(900)
