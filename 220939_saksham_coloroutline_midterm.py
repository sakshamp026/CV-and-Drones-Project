import cv2
import numpy as np

def color_contour(s, target_color='green'):
    
    original_image = cv2.imread(s)

    
    rgb_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

   
    color_thresholds = {
        'green': ([0, 100, 0], [100, 255, 100]),  
        
    }

    lower_bound, upper_bound = color_thresholds.get(target_color, ([0, 0, 0], [0, 0, 0]))

   
    color_mask = cv2.inRange(rgb_image, np.array(lower_bound), np.array(upper_bound))

    
    contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    
    result_image = original_image.copy()
    cv2.drawContours(result_image, contours, -1, (0, 0, 255), 2)  

    
    cv2.imshow('Original Image', cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    cv2.imshow('Contour Image', cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


color_contour('photos\coloroutline.jpg', target_color='green')
