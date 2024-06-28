'''Um codigo para reconhecer e fazer a contagens dos M&Ms de uma imagem. Usei a imagem e como referencia de codigo o repositorio do gitHub "https://github.com/MariaLgA/processamento_objetos.git"'''

import cv2
import numpy

#Carregar uma imagem
img = cv2.imread('mm.webp');

#Redimencionar a imagem para 4:3
newWidth = 640
newHeigth = 480
newSize = (newWidth,newHeigth)

resize = cv2.resize(img,newSize)


#Coversão de cor
imgHsv = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV);

#Mascáras para as cores
blueMask = cv2.inRange(imgHsv, (90, 66, 153), (130, 255, 255));
greenMask = cv2.inRange(imgHsv, (57, 50, 140), (75, 255, 255));
yellowMask = cv2.inRange(imgHsv, (22, 30, 190), (30, 255, 255));
firstBrowMask = cv2.inRange(imgHsv, (140, 15, 80), (180, 91, 215));
secondBrowMask = cv2.inRange(imgHsv, (0, 15, 75), (9, 91, 170));
redMask = cv2.inRange(imgHsv, (150, 40, 130), (180, 255, 255));
orange_mask = cv2.inRange(imgHsv, (3, 70, 100), (13, 255, 255));

# operacao da mascara OR com a mascara marrom
orMaskBrow = cv2.bitwise_or(firstBrowMask, secondBrowMask);

#Kernel: usado para a erosão e dilatação
kernel = numpy.ones((3, 3), numpy.uint8);

#Filtros de erosão nas mascáras para tirar os ruidos das imagens
blueErode = cv2.erode(blueMask, kernel, iterations = 1);
yellowErode = cv2.erode(yellowMask, kernel, iterations = 5);
browErode = cv2.erode(orMaskBrow, kernel, iterations = 2);
redErode = cv2.erode(redMask, kernel, iterations = 1);
orangeErode = cv2.erode(orange_mask, kernel, iterations = 5);

#Filtros de dilatação para preencher os espaços onde são encontradas algumas falhas
blueDilate = cv2.dilate(blueErode, kernel, iterations = 1);
greenDilate = cv2.dilate(greenMask, kernel, iterations = 1);
yellowDilate = cv2.dilate(yellowErode, kernel, iterations = 6);
browDilate = cv2.dilate(browErode, kernel, iterations = 4);
redDilate = cv2.dilate(redErode, kernel, iterations = 1);
orangeDilate = cv2.dilate(orangeErode, kernel, iterations = 6);

#Achandos os m&ms apartir das mascaras e fazendo a sua contagem
cont = 0;
nome = ["azul", "verde", "amarelo", "marrom", "vermelho", "laranja"];
color = [(255, 0, 0), (0, 255, 0), (0, 255, 255), (0, 75, 150), (0, 0, 255), (0, 165, 255)];
array = [blueDilate, greenDilate, yellowDilate, browDilate, redDilate, orangeDilate];

for i in range(len(array)):
    qtd = 0;
    contornos, hieraquia = cv2.findContours(array[i], cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);
    for x in range(len(contornos)):
        area = cv2.contourArea(contornos[x]);
        if(area > 400):
            desenhoContorno = cv2.drawContours(resize, contornos, x, color[i], 2);
            qtd += 1;
    cv2.putText(resize, nome[i] + ": " + str(qtd), (10 + cont, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA);
    cont += 110;

#output da imagem, waitKey para ficar com a imagem travada na tela ate que algum comando a feche
cv2.imshow("original", resize)
cv2.waitKey(0)

#salvar imagem
cv2.imwrite("./imagemAposProcessamento.jpeg", resize)