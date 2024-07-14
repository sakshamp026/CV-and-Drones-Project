import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('Photos\sakshamdp.jpg', cv2.IMREAD_GRAYSCALE)

    
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    
magnitude = np.sqrt(sobelx**2 + sobely**2)

    
magnitude_normalized = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

    
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

   
plt.subplot(122), plt.imshow(magnitude_normalized, cmap='gray')
plt.title('Edge-Detected Image (Sobel Filter)'), plt.xticks([]), plt.yticks([])

plt.show()