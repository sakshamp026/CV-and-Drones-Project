import cv2
import numpy as np

def ig_filter(image_path):
    
    original_image = cv2.imread(image_path)

    
    brightness_factor = 0.5
    darkened_image = cv2.convertScaleAbs(original_image, alpha=1, beta=-127 * (1 - brightness_factor))

    
    contrast_factor = 0.5
    high_contrast_image = cv2.convertScaleAbs(darkened_image, alpha=1 + contrast_factor, beta=0)

    
    hsv_image = cv2.cvtColor(high_contrast_image, cv2.COLOR_BGR2HSV)
    saturation_factor = 0.5
    hsv_image[:,:,1] = np.clip(hsv_image[:,:,1] * (1 + saturation_factor), 0, 127)
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return final_image


input_image_path = 'photos\Tabldg.jpg'
result_image = ig_filter(input_image_path)


cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('Filtered Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
