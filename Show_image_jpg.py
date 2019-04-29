#pip install opencv-python

import cv2
#Carregar e armazanar imagem jpg

imagem = cv2.imread("Croissant.jpg")

#Exibir imagem jpg
lab = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

#gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem JPG", imagem)
#cv2.imshow("Imagem JPG", gray)
cv2.imshow("Imagem JPG", lab)
cv2.waitKey(0)

