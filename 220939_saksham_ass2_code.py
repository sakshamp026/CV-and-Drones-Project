import cv2
import numpy as np


flag = None

def generate():
    global flag

    
    flag = np.zeros((600, 600, 3), dtype=np.uint8)

    
    flag[:200, :] = (0, 165, 255)  
    flag[200:400, :] = (255, 255, 255)  
    flag[400:, :] = (0, 128, 0)
    
    cv2.circle(flag, (300, 300), 100, (255, 0, 0), 2)  
    cv2.circle(flag, (300, 300), 95, (255, 255, 255), -1) 

    
    for i in range(24):
        angle = i * 360 / 24
        
        x1 = 300 + 0 * np.cos(np.radians(angle)) 
        y1 = 300 + 0 * np.sin(np.radians(angle))
        x2 = 300 + 100 * np.cos(np.radians(angle))
        y2 = 300 + 100 * np.sin(np.radians(angle))
        cv2.line(flag, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 1)

    
    cv2.imshow("Indian Flag", flag)
    cv2.waitKey(0)

if __name__ == "__main__":
    generate()

