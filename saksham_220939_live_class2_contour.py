import cv2
import matplotlib.pyplot as plt
import numpy as np

path = r"C:\Users\saksh\OneDrive\Documents\python_CV\photos1\apple.png"
img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (15, 15), 0) 
edged = cv2.Canny(gray, 30, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
img_copy = img.copy()
cv2.drawContours(img, contours,-1, (0, 255, 0), 10) 

cv2.imshow('Contours', img) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 







