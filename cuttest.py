import cv2
x = 100
y = 100
width = 100
height = 100
src = cv2.imread('IMG_4825.JPG',1)
dst = src[y:y+height, x:x+width]
cv2.imwrite('dst.jpg', dst)
print("True")
