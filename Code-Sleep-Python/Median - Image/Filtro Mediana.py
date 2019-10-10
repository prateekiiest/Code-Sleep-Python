# coding: utf-8
# # Filtro Mediana

import cv2 #OpenCV
import numpy as np #biblioteca para trablahar com arrays de forme eficiente
import matplotlib.pyplot as plt # biblioteca para plotar gráficos
import numpy.matlib

img = cv2.imread('Lenna_test_image.png', cv2.IMREAD_GRAYSCALE)
img

plt.figure()
plt.imshow(img, 'gray')
plt.show()
A = img

# Image size
lin, col = np.shape(img)
print(lin)
print(col)

# Create matrix of response
res = np.zeros((lin,col), dtype = np.uint16)
print(res);

i = 15
j = 17
b = [A[i-1,j-1], A[i-1,j] , A[i-1,j+1] , A[i,j-1], A[i,j],A[i,j+1],A[i+1,j-1],A[i+1,j],A[i+1,j+1]]
numpy.median(b)

for i in range (lin - 1):
    for j in range (col - 1):
        b = [A[i-1,j-1], A[i-1,j] , A[i-1,j+1] , A[i,j-1], A[i,j],A[i,j+1],A[i+1,j-1],A[i+1,j],A[i+1,j+1]]
        res[i,j] = numpy.median(b)

plt.imshow(res, 'gray')
plt.show()
cv2.imwrite('mediana.png', res)

