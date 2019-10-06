
# coding: utf-8

# # Filtro Mediana

# In[28]:


import cv2 #OpenCV
import numpy as np #biblioteca para trablahar com arrays de forme eficiente
import matplotlib.pyplot as plt # biblioteca para plotar gráficos
import numpy.matlib


# In[29]:


img = cv2.imread('Lenna_test_image.png', cv2.IMREAD_GRAYSCALE)
img


# In[30]:


plt.figure()
plt.imshow(img, 'gray')
plt.show()
A = img


# In[31]:


# Image size
lin, col = np.shape(img)
print(lin)
print(col)


# In[32]:


# Create matrix of response
res = np.zeros((lin,col), dtype = np.uint16)
print(res);


# In[33]:


i = 15
j = 17
b = [A[i-1,j-1], A[i-1,j] , A[i-1,j+1] , A[i,j-1], A[i,j],A[i,j+1],A[i+1,j-1],A[i+1,j],A[i+1,j+1]]
numpy.median(b)


# In[34]:


for i in range (lin - 1):
    for j in range (col - 1):
        b = [A[i-1,j-1], A[i-1,j] , A[i-1,j+1] , A[i,j-1], A[i,j],A[i,j+1],A[i+1,j-1],A[i+1,j],A[i+1,j+1]]
        res[i,j] = numpy.median(b)


# In[35]:


plt.imshow(res, 'gray')
plt.show()
cv2.imwrite('mediana.png', res)

