from matplotlib import pyplot as plt
import cv2
import numpy as np

#parâmetros da intensidade
k = 1
gama_maior_1 = 1.2
gama_menor_1 = 0.75

# Carregar e armazenar imagem jpg

imagem1 = cv2.imread("Croissant.jpg")
imagem2 = cv2.imread("Croissant.jpg")

# get b,g,r
(canalAzul1, canalVerde1, canalVermelho1) = cv2.split(imagem1)
(canalAzul2, canalVerde2, canalVermelho2) = cv2.split(imagem2)
# rotina para gerar imagem em tons de cinza
for x in range(0, imagem1.shape[0]):  # percorre linhas da imagem
    for y in range(0, imagem1.shape[1]):  # percorre colunas da imagem

        # média aritmética dos canais RGB e arredondamento para inteiro e transformacao da intensidade gama_maior_1
        imagem1[x, y] = k*(np.round((canalAzul1[x, y] + canalVerde1[x, y] + canalVermelho1[x, y]) / 3, 0))**gama_maior_1
        #print(imagem[x, y][0])

for x in range(0, imagem2.shape[0]):  # percorre linhas da imagem
    for y in range(0, imagem2.shape[1]):  # percorre colunas da imagem

        # média aritmética dos canais RGB e arredondamento para inteiro e transformacao da intensidade gama_menor_1
        imagem2[x, y] = k*(np.round((canalAzul2[x, y] + canalVerde2[x, y] + canalVermelho2[x, y]) / 3, 0))**gama_menor_1
        #print(imagem[x, y][0])

# Exibir imagem com transformacao de intensidade gama_maior_1
cv2.imshow("Imagem com gama maior que 1", imagem1)

# Exibir imagem com transformacao de intensidade gama_menor_1
cv2.imshow("Imagem com gama menor que 1", imagem2)
cv2.waitKey(0)

plt.figure()
#plt.title("Histograma tons de cinza")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot()
#plt.xlim([0, 256])
plt.show()