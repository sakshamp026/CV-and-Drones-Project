import cv2
imprt numpy as np

image = cv2.imread('Photos\scenery.jpg')
brightness_factor = 0.5
darkened_image = cv2.convertScaleAbs(image, alpha=1, beta=-255 * (1 - brightness_factor))

    
contrast_factor = 1.5
high_contrast_image = cv2.convertScaleAbs(darkened_image, alpha=contrast_factor, beta=0)

    
hsv_image = cv2.cvtColor(high_contrast_image, cv2.COLOR_BGR2HSV)
saturation_factor = 1.5
hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] * saturation_factor, 0, 255)
final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)




input_image_path = 'path/to/your/image.jpg'
result_image = ig_filter(input_image_path)


cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Filtered Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()