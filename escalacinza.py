import cv2
import numpy as np

# Carregar e armazenar imagem jpg

imagem = cv2.imread("Croissant.jpg")

# get b,g,r
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)


for y in range(0, imagem.shape[0]): #percorre linhas
    for x in range(0, imagem.shape[1]): #percorre colunas
        #média aritmética dos canais RGB e arredondamento para inteiro
        imagem[y, x] = np.round((canalAzul[y, x] + canalVerde[y, x] + canalVermelho[y, x])/3, 0)

# Exibir imagem jpg
cv2.imshow("Imagem com Tom Cinza", imagem)
cv2.waitKey(0)
