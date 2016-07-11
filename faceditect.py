import cv2

#顔検出器をロード
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
#入力画像の読み込み
img = cv2.imread('input2.jpg')
#gray scaleヘ変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
#顔検出
faces = face_cascade.detectMultiScale(gray, 1.3, 5)     
#赤枠

for (x,y,w,h) in faces:
     dst = img[y:y+h, x:x+w]
     cv2.imwrite('test.jpg',dst)
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
     print("x:" + str(x))
     print("y:" + str(y))
     print("width:" + str(w))
     print("height:" + str(h))
#結果の表示
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
