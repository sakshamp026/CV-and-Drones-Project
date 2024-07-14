import cv2 as cv
import matplotlib.image as mpimg
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# img = cv.imread('Photos/sakshamdp.jpg')

input_img = np.array(Image.open('Photos/sakshamdp.jpg'))
print(input_img.shape)

image = cv.imread('Photos/sakshamdp.jpg')  # reads in BGR format
print(image.shape)

plt.imshow(image)
plt.show()

img = image[:,:,[2,1,0]] #converted to RGB
plt.imshow(img)
plt.axis("off")
plt.show()


img = cv.imread('Photos\sakshamdp.jpg',0)  # 0 flag reads image in grayscale
print(img.shape)
plt.imshow(img,cmap='gray')
plt.axis("off")
plt.show()

plt.imshow(img, cmap='magma')
plt.colorbar()
plt.show()





img_orig= cv.imread('Photos\sakshamdp.jpg')
#convert to grayscale
img_gray = cv.cvtColor(img_orig, cv.COLOR_BGR2GRAY)
#convert to rgb
img_rgb = cv.cvtColor(img_orig, cv.COLOR_BGR2RGB)

img_blue_channel = img_orig[:,:,0]
img_green_channel = img_orig[:,:,1]
img_red_channel = img_orig[:,:,2]

img_blue = np.copy(img_rgb)
img_green = np.copy(img_rgb)
img_red = np.copy(img_rgb)

img_blue[:,:,[0,1]]=0
img_green[:,:,[0,2]]=0
img_red[:,:,[1,2]]=0


plt.figure(figsize = (12,12))

plt.subplot(3,3,1)
plt.imshow(img_rgb)
plt.axis("off")
plt.title("RGB")

plt.subplot(3,3,2)
plt.imshow(img_gray, cmap="gray")
plt.axis("off")
plt.title("Grayscale")


plt.subplot(3, 3, 3)
plt.imshow(img_gray, cmap="plasma")
plt.axis("off")
plt.title("Thermal")


plt.subplot(3, 3, 4)
plt.imshow(img_red)
plt.axis("off")
plt.title("Red channel")


plt.subplot(3, 3, 5)
plt.imshow(img_green)
plt.axis("off")
plt.title("Green channel")


plt.subplot(3, 3, 6)
plt.imshow(img_blue)
plt.axis("off")
plt.title("Blue channel")


plt.subplot(3, 3, 7)
plt.imshow(img_red_channel, cmap="gray")
plt.axis("off")
plt.title("Red channel as grayscale")


plt.subplot(3, 3, 8)
plt.imshow(img_green_channel, cmap="gray")
plt.axis("off")
plt.title("Green channel as grayscale")


plt.subplot(3, 3, 9)
plt.imshow(img_blue_channel, cmap="gray")
plt.axis("off")
plt.title("Blue channel as grayscale")


plt.show()