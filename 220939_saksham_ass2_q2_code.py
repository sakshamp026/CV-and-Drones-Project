import cv2
import numpy as np


flag = None
flag_90 = None
flag_180 = None
flag_270 = None

def rotate(img, y):
    
    height, width = img.shape[:2]

    
    M = cv2.getRotationMatrix2D((width / 2, height / 2), y, 1)

    
    rotated = cv2.warpAffine(img, M, (width, height))

    return rotated

def generate():
    global flag, flag_90, flag_180, flag_270

    
    generate_initial_flag()

    
    flag_90 = rotate(flag.copy(), 90)
    flag_180 = rotate(flag.copy(), 180)
    flag_270 = rotate(flag.copy(), 270)

def generate_initial_flag():
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

    
    

    

if __name__ == "__main__":
    generate()

    
    cv2.imshow("Indian Flag 0", flag)
    cv2.imshow("Indian Flag 90", flag_90)
    cv2.imshow("Indian Flag 180", flag_180)
    cv2.imshow("Indian Flag 270", flag_270)
    cv2.waitKey(0)
