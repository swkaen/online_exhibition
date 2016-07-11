import cv2

if __name__=="__main__":

    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    body_cascade = cv2.CascadeClassifier('/usr/local/Cellar/opencv3/3.0.0/share/OpenCV/haarcascades/haarcascade_fullbody.xml')
    lgh = cv2.imread('laughing_man.jpg')
    if capture.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)

    while True:

        ret, image = capture.read()
        if ret == False:
            continue
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100,100))
        for (x,y,w,h) in faces:
            dst = image[y:y+h, x:x+w]
            print(x,y,w,h) 
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow("Capture", image)

        if len(faces) != 0:
            cv2.imwrite("image.png", image)
            break
        

        if cv2.waitKey(10) >= 0:
            cv2.imwrite("image.png", image)
            break

    cv2.destroyAllWindows()
