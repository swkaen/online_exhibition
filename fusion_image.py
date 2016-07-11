from twitter_access import *
from PIL import Image
import sys
import cv2
import os


face_x  = 0
face_y  = 0
thumb_w = 0
thumb_h = 0
MY_SCREEN_NAME = sys.argv[1]
#BASE_IMAGE_NAME = sys.argv[2]
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Twitter access
secret_json = {
  "access_token": "",
  "access_token_secret": "",
  "consumer_key":"" ,
  "consumer_secret":"" }

t = twitter_access(secret_json)
profile = get_user_profile(t, MY_SCREEN_NAME)
image_saver(profile)

#使うカメラの設定(数字で指定)
capture = cv2.VideoCapture(0)
if capture.isOpened() is False:
        raise("IO Error")
cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

while True:

        ret, image = capture.read()
        if ret == False:
            continue
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100,100))
#        for (x,y,w,h) in faces:
#            dst = image[y:y+h, x:x+w]
#            print(x,y,w,h)
#            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Capture", image)

        if len(faces) != 0:
            cv2.imwrite("image.png", image)
            for (x,y,w,h) in faces:
                    face_x  = x
                    face_y  = y
                    thumb_w = w
                    thumb_h = h
            break


        if cv2.waitKey(10) >= 0:
            cv2.imwrite("image.png", image)
            break

cv2.destroyAllWindows()



base_img = Image.open("image.png")


thumb = Image.open(MY_SCREEN_NAME+".png")
thumb = thumb.resize((thumb_h, thumb_w))

base_img.paste(thumb, (face_x, face_y))
base_img.save(MY_SCREEN_NAME+"f.jpg")
os.system('open ' + MY_SCREEN_NAME + "f.jpg")
#img_show = cv2.imread(MY_SCREEN_NAME+"f.jpg")
#cv2.imshow('img',img_show)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
