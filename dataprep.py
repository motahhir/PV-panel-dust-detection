import os 
import cv2
from matplotlib import pyplot as plt


path=r'C:\Users\Asus\Desktop\projet\data\images'
os.listdir(path)

for index,img in enumerate(os.listdir(path)):
    img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
    ret, thresh = cv2.threshold(img_array, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.imsave(f'{index}.png',thresh, cmap='gray')