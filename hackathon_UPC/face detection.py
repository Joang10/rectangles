import numpy as np
import random
import cv2
import time

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier('faces.xml')
random.seed
cap = cv2.VideoCapture(0)
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
count = 0
vides = 5

ho =random.randint(50, 150)
wo =random.randint(50, 150)
posx = random.randint(50, gray.shape[1] - 50)
posy = random.randint(50, gray.shape[0] - 50)
tim = time()
while 1:
    cube = 1
    timer = 1
    print(img.shape)
    tempo = 0



    while cube and timer:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        prevtim = tim
        tim = time()
        tempo = prevtim-tim

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        prob = random.randint(0,100)
        if (prob <= 80 ):
            cv2.rectangle(img, (posx, posy), (posx + wo, posy + ho), (0, 255, 0), cv2.FILLED)
        elif(prob <= 90):
            cv2.rectangle(img, (posx, posy), (posx + wo, posy + ho), (0, 0, 255), cv2.FILLED)
        elif (prob <= 95):
            cv2.rectangle(img, (posx, posy), (posx + wo, posy + ho), (0, 0, 0), cv2.FILLED)
        else:
            cv2.rectangle(img, (posx, posy), (posx + wo, posy + ho), (255, 255, 255), cv2.FILLED)


        if (x<=posx<=(x+w) and y<=posy<=(y+h)) or (x<=posx<=(x+w) and y<=posy+ho<=(y+h)) or (x<=posx+wo<=(x+w) and y<=posy<=(y+h)) or (x<=posx+wo<=(x+w) and y<=posy+ho<=(y+h)):
            cube = 0
            count += 1

        vertical_img = cv2.flip(img, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.rectangle(vertical_img, (7, 3), (200,37), (0, 0, 0), cv2.FILLED)
        cv2.rectangle(vertical_img, (393, 3), (550,37), (0, 0, 0), cv2.FILLED)
        cv2.putText(vertical_img, 'Points: '+str(count), (15, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(vertical_img, 'Lifes: ', (400, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(vertical_img, str(vides), (505, 30), font, 1, ((50*vides), (50*vides), (50*vides)), 2, cv2.LINE_AA)
        cv2.imshow('img', vertical_img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    ho =random.randint(50, 150)
    wo =random.randint(50, 150)
    while(((x<=posx<=(x+w) and y<=posy<=(y+h)) or (x<=posx<=(x+w) and y<=posy+ho<=(y+h)) or (x<=posx+wo<=(x+w) and y<=posy<=(y+h)) or (x<=posx+wo<=(x+w) and y<=posy+ho<=(y+h)))==1):
        posx = random.randint(50, gray.shape[1]-50)
        posy = random.randint(50, gray.shape[0]-50)


cap.release()
cv2.destroyAllWindows()