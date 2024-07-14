import cv2
import numpy as np

def reduce_brightness(image_path):
    # Read the input image
    original_image = cv2.imread(image_path)

    # Reduce brightness to 0.5 of its initial value
    brightness_factor = 0.5
    darkened_image = cv2.convertScaleAbs(original_image, alpha=1, beta=-127 * (1 - brightness_factor))

    # Display the original and darkened images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Darkened Image', darkened_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example Usage:
input_image_path = 'photos\Tabldg.jpg'
reduce_brightness(input_image_path)
