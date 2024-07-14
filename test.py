import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread('Photos\sakshamdp.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Photos\dp2.jpg', cv2.IMREAD_GRAYSCALE)

   
img1 = cv2.resize(img1, (256, 256))
img2 = cv2.resize(img2, (256, 256))

    
f_transform1 = np.fft.fft2(img1)
f_transform2 = np.fft.fft2(img2)
rows, cols = img1.shape
center_row, center_col = rows // 2, cols // 2
radius = 30  
mask = np.ones((rows, cols), np.uint8)
cv2.circle(mask, (center_col, center_row), radius, 0, -1)

   
f_transform1_lpf = f_transform1 * mask
f_transform2_lpf = f_transform2 * mask

    
img1_lpf = np.abs(np.fft.ifft2(f_transform1_lpf)).astype(np.uint8)
img2_lpf = np.abs(np.fft.ifft2(f_transform2_lpf)).astype(np.uint8)

   
plt.subplot(231), plt.imshow(np.log(1 + np.abs(f_transform1)), cmap='gray')
plt.title('Fourier Transform - Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(232), plt.imshow(np.log(1 + np.abs(f_transform1_lpf)), cmap='gray')
plt.title('Fourier after LPF - Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(233), plt.imshow(img1_lpf, cmap='gray')
plt.title('Modified Image after LPF - Image 1'), plt.xticks([]), plt.yticks([])

plt.subplot(234), plt.imshow(np.log(1 + np.abs(f_transform2)), cmap='gray')
plt.title('Fourier Transform - Image 2'), plt.xticks([]), plt.yticks([])

plt.subplot(235), plt.imshow(np.log(1 + np.abs(f_transform2_lpf)), cmap='gray')
plt.title('Fourier after LPF - Image 2'), plt.xticks([]), plt.yticks([])

plt.subplot(236), plt.imshow(img2_lpf, cmap='gray')
plt.title('Modified Image after LPF - Image 2'), plt.xticks([]), plt.yticks([])

plt.show()

    
hybrid_image = cv2.addWeighted(img1_lpf, 0.5, img2_lpf, 0.5, 0)

    
plt.imshow(hybrid_image, cmap='gray')
plt.title('Combined Hybrid Image')
plt.show()