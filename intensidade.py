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
saida_intensidade1 = []
entrada_intensidade1 = []
saida_intensidade2 = []
entrada_intensidade2 = []

for x in range(0, imagem1.shape[0]):  # percorre linhas da imagem
    for y in range(0, imagem1.shape[1]):  # percorre colunas da imagem

        entrada_r1 = np.round((canalAzul1[x, y] + canalVerde1[x, y] + canalVermelho1[x, y]) / 3, 0)
        # média aritmética dos canais RGB e arredondamento para inteiro e transformacao da intensidade gama_maior_1
        imagem1[x, y] = k*entrada_r1**gama_maior_1

        entrada_intensidade1.append(entrada_r1)
        saida_intensidade1.append(imagem1[x, y][0])


for x in range(0, imagem2.shape[0]):  # percorre linhas da imagem
    for y in range(0, imagem2.shape[1]):  # percorre colunas da imagem
        entrada_r2 = np.round((canalAzul2[x, y] + canalVerde2[x, y] + canalVermelho2[x, y]) / 3, 0)
        # média aritmética dos canais RGB e arredondamento para inteiro e transformacao da intensidade gama_menor_1
        imagem2[x, y] = k*entrada_r2**gama_menor_1

        entrada_intensidade2.append(entrada_r2)
        saida_intensidade2.append(imagem2[x, y][0])

# Exibir imagem com transformacao de intensidade gama_maior_1
cv2.imshow("Imagem com gama maior que 1", imagem1)

# Exibir imagem com transformacao de intensidade gama_menor_1
cv2.imshow("Imagem com gama menor que 1", imagem2)
cv2.waitKey(0)

#rotina para contagem de quantidade de cores presente nos pixels da imagem
#histograma da imagem com gama maior que 1
qtd_cores1 = []
for i in range(0, 255):  # cor
    conferecor = 0

    for x in range(0, imagem1.shape[0]):  # percorre linhas da imagem
        for y in range(0, imagem1.shape[1]):  # percorre colunas da imagem

            if i == imagem1[x, y][0]:  # um dos valores rgb em tons de cinza
                conferecor += 1
    qtd_cores1.append(conferecor)

#plot do histograma com gama maior que 1
plt.figure()
plt.title("Histograma com gama maior que 1")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(qtd_cores1)
plt.xlim([0, 256])
plt.show()


#histograma da imagem com gama menor que 1
qtd_cores2 = []
for i in range(0, 255):  # cor
    conferecor = 0

    for x in range(0, imagem2.shape[0]):  # percorre linhas da imagem
        for y in range(0, imagem2.shape[1]):  # percorre colunas da imagem

            if i == imagem2[x, y][0]:  # um dos valores rgb em tons de cinza
                conferecor += 1
    qtd_cores2.append(conferecor)

#plot do histograma com gama menor que 1
plt.figure()
plt.title("Histograma com gama menor que 1")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(qtd_cores2)
plt.xlim([0, 256])
plt.show()


#plot funcao de mapeamento1
plt.figure()
plt.title("Função de mapeamento gama maior que 1")
plt.xlabel("Intensidade entrada")
plt.ylabel("Intensidade saida")
plt.plot(entrada_intensidade1, saida_intensidade1)
plt.show()

#plot funcao de mapeamento2
plt.figure()
plt.title("Função de mapeamento gama menor que 1")
plt.xlabel("Intensidade entrada")
plt.ylabel("Intensidade saida")
plt.plot(entrada_intensidade2, saida_intensidade2)
plt.show()