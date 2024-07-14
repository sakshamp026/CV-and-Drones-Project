import cv2
import numpy as np
import matplotlib.pyplot as plt

def hough_line(s):
    
    original_image = cv2.imread(s)
    

    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    

    edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)
    

    lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)
    
    result_image = original_image.copy()
    
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            
            cv2.line(result_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    
    plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)), plt.title('Detected Lines')
    plt.show()


hough_line('photos\Tabldg.jpg')
