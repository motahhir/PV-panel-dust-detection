import os 
import cv2
from matplotlib import pyplot as plt
import numpy as np
from skimage.feature import greycomatrix, greycoprops

#extracting relevant GLCM matrix feature for automatic classification of solar panels
def contrast_feature(matrix_coocurrence):
    contrast = greycoprops(matrix_coocurrence, 'contrast')
    return np.mean(contrast)

path=r'C:\Users\Asus\Desktop\projet\data\images'
os.listdir(path)

#thresholding images using Otsu's segmentation and classification using a basis contrast of value of 11
for index,img in enumerate(os.listdir(path)):
    img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(img_array, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    bins = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255])
    inds = np.digitize(thresh, bins)
    max_value = inds.max()+1
    matrix_coocurrence = greycomatrix(inds, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value, normed=False, symmetric=False)
    with open('values.txt', 'a') as f:
                f.write("image "+str(index)+"contrast value: "+str(contrast_feature(matrix_coocurrence))+"\n")
    if (contrast_feature(matrix_coocurrence))>=11:
        plt.imsave(f'dirty/{index}.png',thresh, cmap='gray')
    else:
        plt.imsave(f'clean/{index}.png',thresh,cmap='gray')

#renaming files in a sequential manner
path1='clean/'
path2='dirty/'
i=0
j=0
for image in os.listdir(path1):
    os.rename(path1+image,path+f'{i}.png')
    i+=1

for image in os.listdir(path2):
    os.rename(path2+image,path+f'{j}.png')
    j+=1
    