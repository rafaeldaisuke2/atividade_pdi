import cv2

# Carregar e armazanar imagem jpg

imagem = cv2.imread("Croissant.jpg")

# Exibir imagem jpg

#cv2.imshow("Imagem JPG", imagem)

for y in range(0, imagem.shape[0]):  # percorre linhas
    for x in range(0, imagem.shape[1]):  # percorre colunas
        
cv2.imshow("Imagem modificada", imagem)
cv2.waitKey(0)
