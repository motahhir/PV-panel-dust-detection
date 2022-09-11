import numpy as np
import cv2
from skimage.feature import greycomatrix, greycoprops
from skimage import io, color, img_as_ubyte
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from matplotlib import pyplot as plt
import pandas as pd

def contrast_feature(matrix_coocurrence):
    contrast = greycoprops(matrix_coocurrence, 'contrast')
    return np.mean(contrast)

def dissimilarity_feature(matrix_coocurrence):
    dissimilarity = greycoprops(matrix_coocurrence, 'dissimilarity')    
    return np.mean(dissimilarity)

def homogeneity_feature(matrix_coocurrence):
    homogeneity = greycoprops(matrix_coocurrence, 'homogeneity')
    return np.mean(homogeneity)

def energy_feature(matrix_coocurrence):
    energy = greycoprops(matrix_coocurrence, 'energy')
    return  np.mean(energy)

def correlation_feature(matrix_coocurrence):
    correlation = greycoprops(matrix_coocurrence, 'correlation')
    return  np.mean(correlation)

def asm_feature(matrix_coocurrence):
    asm = greycoprops(matrix_coocurrence, 'ASM')
    return  np.mean(asm)

class Photo:
    df=pd.DataFrame(columns = ['Contrast','Dissimilarity','Homogeneity','Energy','Correlation','ASM'])
    def __init__(self, path):
        self.path=path
        self.matrix_coocurrence=self.computeGLCM()
        
    def display(self):
        plt.tight_layout()
        plt.show()
        
    def segmentation(self):
        img = cv2.imread(self.path)
        input_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) 
        plt.subplot(121), plt.imshow(input_img)
        plt.title('Input Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(thresh,'gray')
        plt.imsave(r'thresh.png',thresh)
        plt.title('Thresholded image'), plt.xticks([]), plt.yticks([])
    
    def computeGLCM(self):
        imgthresh='thresh.png'
        img = cv2.imread(imgthresh,0)
        bins = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255])
        inds = np.digitize(img, bins)
        max_value = inds.max()+1
        return greycomatrix(inds, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value, normed=False, symmetric=False)
    
    def checkfordust(self):
        return (contrast_feature(self.matrix_coocurrence)>0.7)
     
    def append2df(self):
        Photo.df=Photo.df.append({'Contrast':contrast_feature(self.matrix_coocurrence), 'Dissimilarity':dissimilarity_feature(self.matrix_coocurrence),
                                  'Homogeneity':homogeneity_feature(self.matrix_coocurrence), 'Energy': energy_feature(self.matrix_coocurrence),
                                  'Correlation':correlation_feature(self.matrix_coocurrence),'ASM':asm_feature(self.matrix_coocurrence)},ignore_index=True)
        return Photo.df