#pip install opencv-python

import cv2

#Carregar e armazanar imagem jpg
imagem = cv2.imread("Croissant.jpg")

#Exibir imagem jpg

cv2.imshow("Imagem original colorida JPG", imagem)

cv2.waitKey(0)

