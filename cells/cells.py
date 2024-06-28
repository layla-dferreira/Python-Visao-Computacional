'''Um codigo para reconhecer celulas brancas de uma imagem. Usei a imagem e como referencia de codigo o repositorio do gitHub "https://github.com/MariaLgA/processamento_objetos.git"'''

import cv2
import numpy

#Carregar a imagem
img = cv2.imread('cells/img_original.jpg');

#Coversão de cor
imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV);

#Mascara pra as cores 
imgColor = cv2.inRange(imgHsv, (130, 80, 180), (150, 255, 255));

#Kernel
kernel = numpy.ones((3, 3), numpy.uint8);

#Filtro de erosão
imgErode = cv2.erode(imgColor, kernel, iterations = 3);

#Fitro de dilatação
imgDilate = cv2.dilate(imgErode, kernel, iterations = 5);

#Contornos
cont = 0
contornos, hierarquia = cv2.findContours(imgDilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);

for i in range(len(contornos)):
    area = cv2.contourArea(contornos[i]);
    if(area > 1000):
        #desenho dos contornos
        desenhoContorno = cv2.drawContours(img, contornos, i, (0, 0, 0), 2);
        cont += 1;
cv2.putText(img,"celulas brancas" + ": "+ str(cont), (40, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA);

#output da imagem
cv2.imshow("imagem final processada",img);
cv2.waitKey(0);

cv2.imwrite("./celulasProcessadas.jpeg",img);