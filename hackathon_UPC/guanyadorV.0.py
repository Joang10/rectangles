import random
import cv2
import time
import pygame
import os
from pygame.locals import *

soundvece = ["encert/nice-work.wav"]
soundvecb = ["blanc/willy.wav"]
soundvecp = ["perdre/ooooh.wav","perdre/poor-baby.wav"]
soundvect = ["temps/ridiculous.wav","temps/urghhh.wav","temps/wait-a-minute.wav","temps/what-2.wav"]
soundvecv = ["vida/that-feels-really-powerful.wav","vida/this-is-delicious.wav","vida/unbelievable.wav"]
pygame.mixer.init()

print(len(soundvece) - 1)
pygame.mixer.music.load(soundvece[random.randint(0, len(soundvece) - 1)])
pygame.mixer.music.play(0)


# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('faces.xml')
random.seed
cap = cv2.VideoCapture(0)

while 1:
    inst = cv2.imread('instructions.png', 3)
    cv2.imshow('img', inst)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
os.system('afplay 3.wav')
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = 0
vides = 5




ho = random.randint(50, 150)
wo = random.randint(50, 150)
posx = random.randint(50, gray.shape[1] - 50)
posy = random.randint(50, gray.shape[0] - 50)
tim = time.time()
tempo = 0
game = 1
while game:
    cube = 1
    timer = 1
    tempo = 0
    sumatempo = 0
    miss = 0
    prob = random.randint(0, 100)
    if (prob <= 80):
        color = (0, 255, 0)
        tempscub = 3
    elif (prob <= 90):
        color = (0, 0, 255)
        tempscub = 3
    elif (prob <= 95):
        color = (0, 0, 0)
        tempscub = 3
    else:
        color = (255, 255, 255)
        tempscub = 3


    while cube and timer:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        prevtim = tim
        tim = time.time()
        tempo = tim - prevtim
        sumatempo +=tempo
        print(tempo)
        if sumatempo > tempscub:
            timer = 0
            miss = 1
            print('agotated')

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        cv2.rectangle(img, (posx, posy), (posx + wo, posy + ho), color, cv2.FILLED)



        if (x <= posx <= (x + w) and y <= posy <= (y + h)) or (x <= posx <= (x + w) and y <= posy + ho <= (y + h)) or (
                    x <= posx + wo <= (x + w) and y <= posy <= (y + h)) or (
                    x <= posx + wo <= (x + w) and y <= posy + ho <= (y + h)):
            cube = 0
            count += 1
            if color == (0, 0, 255):
                vides += 1
                pygame.mixer.music.load(soundvecv[random.randint(0, len(soundvecv) - 1)])
                pygame.mixer.music.play(0)

            if color == (0, 0, 0):
                vides -= 2
                pygame.mixer.music.load(soundvecp[random.randint(0, len(soundvecp) - 1)])
                pygame.mixer.music.play(0)

            if color == (255, 255, 255):
                pygame.mixer.music.load(soundvecb[random.randint(0, len(soundvecb) - 1)])
                pygame.mixer.music.play(0)


        vertical_img = cv2.flip(img, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(vertical_img, (7, 3), (200, 37), (0, 0, 0), cv2.FILLED)
        cv2.rectangle(vertical_img, (393, 3), (550, 37), (0, 0, 0), cv2.FILLED)
        cv2.putText(vertical_img, 'Points: ' + str(count), (15, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(vertical_img, 'Lifes: ', (400, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(vertical_img, str(vides), (505, 30), font, 1, ((50 * vides), (50 * vides), 255), 2,cv2.LINE_AA)
        cv2.imshow('img', vertical_img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        if miss:
            if color == (0, 255, 0):
                vides -= 1
                pygame.mixer.music.load(soundvect[random.randint(0, len(soundvect) - 1)])
                pygame.mixer.music.play(0)
                posx = random.randint(50, gray.shape[1] - 50)
                posy = random.randint(50, gray.shape[0] - 50)

    ho = random.randint(50, 150)
    wo = random.randint(50, 150)
    while (((x <= posx <= (x + w) and y <= posy <= (y + h)) or (x <= posx <= (x + w) and y <= posy + ho <= (y + h)) or (
                x <= posx + wo <= (x + w) and y <= posy <= (y + h)) or (
                x <= posx + wo <= (x + w) and y <= posy + ho <= (y + h))) == 1):
        posx = random.randint(50, gray.shape[1] - 50)
        posy = random.randint(50, gray.shape[0] - 50)

    if vides <= 0:
        game = 0
        pygame.mixer.music.load("GRANFINAL.wav")
        pygame.mixer.music.play(0)
        victori = cv2.imread('victory_royale.jpg', 3)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(victori, (110, 630), (900, 770), (0, 0, 0), cv2.FILLED)
        cv2.putText(victori, 'LOSER, JUST: ' +str(count) + ' POINTS', (130, 700), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        cv2.imshow('img', victori)
        k = cv2.waitKey(30) & 0xff
        time.sleep(10)



cap.release()
cv2.destroyAllWindows()