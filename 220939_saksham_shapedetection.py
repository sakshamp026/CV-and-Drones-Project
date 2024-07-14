import cv2
import numpy as np

def get_shape_name(approx):
    num_sides = len(approx)
    if num_sides == 3:
        return "Triangle"
    elif num_sides == 4:
        return "Rectangle"
    elif num_sides == 5:
        return "Pentagon"
    elif num_sides == 6:
        return "Hexagon"
    elif num_sides == 7:
        return "Heptagon"
    elif num_sides == 8:
        return "Octagon"
    elif num_sides == 9:
        return "Nonagon"
    elif num_sides >= 10:
        return "Circle"
    else:
        return "Unknown"

def shape(s):
    
    original_image = cv2.imread(s)
    
    
    image = cv2.imread(s, cv2.IMREAD_GRAYSCALE)
    
    
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    image_with_shapes = original_image.copy()
    
    for index, contour in enumerate(contours):
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        shape_name = get_shape_name(approx)

        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        cv2.drawContours(image_with_shapes, [contour], -1, (0, 255, 0), 2)
        cv2.putText(image_with_shapes, shape_name, (cX - 20, cY - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        
        cv2.circle(image_with_shapes, (cX, cY), 5, (0, 0, 255), -1)

        print(f"Shape {index + 1}: {shape_name} at center ({cX}, {cY})")

   
    cv2.imshow("Original Image", original_image)
    cv2.imshow("Image with Shapes", image_with_shapes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


shape("photos\shapes.jpg")
