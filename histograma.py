
from matplotlib import pyplot as plt
import cv2
import numpy as np

# Carregar e armazenar imagem jpg

imagem = cv2.imread("Croissant.jpg")

# get b,g,r
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)

#rotina para gerar imagem em tons de cinza
for x in range(0, imagem.shape[0]): #percorre linhas da imagem
    for y in range(0, imagem.shape[1]): #percorre colunas da imagem

        #média aritmética dos canais RGB e arredondamento para inteiro
        imagem[x, y] = np.round((canalAzul[x, y] + canalVerde[x, y] + canalVermelho[x, y])/3, 0)
        #print(imagem[x, y])

# Exibir imagem jpg
#cv2.imshow("Imagem com Tom Cinza", imagem)
#cv2.waitKey(0)
conferecor = []

for i in range(0, 255): #cor
    for x in range(0, imagem.shape[0]): #percorre linhas da imagem
        for y in range(0, imagem.shape[1]): #percorre colunas da imagem
            if i == imagem[x, y][0]: #um dos valores rgb em tons de cinza
                conferecor[i] += 1



print(confere_cor)
