import cv2
import numpy as np

def solve(s):
    img = cv2.imread(s)
    img = cv2.GaussianBlur(img,(5,5),0)
    t_lower = 50
    t_upper = 150
    edge = cv2.Canny(img, t_lower, t_upper)
    
    cv2.imshow("Original", img)
    cv2.imshow("Edges", edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
s = r"C:\Users\saksh\OneDrive\Documents\python_CV\photos1\lambo.JPG"

solve(s)

