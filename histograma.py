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
        #print(imagem[x, y][0])


#rotina para contagem de quantidade de cores presente nos pixels da imagem
qtd_cores = []
for i in range(0, 255):  # cor
    conferecor = 0

    for x in range(0, imagem.shape[0]):  # percorre linhas da imagem
        for y in range(0, imagem.shape[1]):  # percorre colunas da imagem

            if i == imagem[x, y][0]:  # um dos valores rgb em tons de cinza
                conferecor += 1
    qtd_cores.append(conferecor)

#print(qtd_cores)

#plot do histograma em tons de cinza
plt.figure()
plt.title("Histograma tons de cinza referência")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(qtd_cores)
plt.xlim([0, 256])
plt.show()

#[815, 1124, 1231, 1149, 1198, 1167, 1115, 1186, 1176, 1089, 1101, 1074, 1073, 1095, 1102, 1104, 1079, 1066, 1078, 1110, 1046, 1035, 1061, 1013, 1019, 1021, 969, 974, 986, 956, 944, 919, 967, 885, 915, 872, 907, 871, 965, 908, 832, 887, 898, 884, 939, 987, 944, 1002, 978, 1021, 1023, 1015, 1037, 1002, 1130, 1052, 1151, 1177, 1096, 1144, 1185, 1200, 1249, 1132, 1191, 1278, 1302, 1387, 1401, 1433, 1496, 1494, 1466, 1586, 1647, 1710, 1783, 2028, 2193, 2190, 2519, 3047, 4349, 6821, 140262, 783, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
