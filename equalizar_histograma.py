from matplotlib import pyplot as plt
import cv2
import numpy as np

# Carregar e armazenar imagem jpg

imagem = cv2.imread("Croissant.jpg")

# get b,g,r
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)

# rotina para gerar imagem em tons de cinza
for x in range(0, imagem.shape[0]):  # percorre linhas da imagem
    for y in range(0, imagem.shape[1]):  # percorre colunas da imagem

        # média aritmética dos canais RGB e arredondamento para inteiro
        imagem[x, y] = np.round((canalAzul[x, y] + canalVerde[x, y] + canalVermelho[x, y]) / 3, 0)
        # print(imagem[x, y][0])

# rotina para contagem de quantidade de cores presente nos pixels da imagem
# histograma
qtd_cores = []
for i in range(0, 255):  # cor
    conferecor = 0

    for x in range(0, imagem.shape[0]):  # percorre linhas da imagem
        for y in range(0, imagem.shape[1]):  # percorre colunas da imagem

            if i == imagem[x, y][0]:  # um dos valores rgb em tons de cinza
                conferecor += 1
    qtd_cores.append(conferecor)

#
# #imagem equalizada
# img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# h_eq = cv2.equalizeHist(img)
# cv2.imshow("Imagem equalizada", h_eq)
# cv2.waitKey(0)

# histograma equalizado
cores_mapeadas = []
for j in range(0, 255):
    s = np.round((qtd_cores[j] * 255) / (imagem.shape[0] * imagem.shape[1]), 0)
    cores_mapeadas.append(s)

# plot do histograma equalizado
plt.figure()
plt.title("Histograma equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(cores_mapeadas)
plt.xlim([0, 256])
plt.show()

for i in range(0, 255):
    for x in range(0, imagem.shape[0]):  # percorre linhas da imagem
        for y in range(0, imagem.shape[1]):  # percorre colunas da imagem
            if i == imagem[x, y][0]:
                imagem[x, y] = [cores_mapeadas[i], cores_mapeadas[i], cores_mapeadas[i]]

cv2.imshow("Imagem Equalizada", imagem)

cv2.waitKey(0)
