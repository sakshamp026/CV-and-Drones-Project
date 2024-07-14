import cv2
import cv2.aruco as aruco
import numpy as np


camera_matrix = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float32)
dist_coeffs = np.array([k1, k2, p1, p2, k3], dtype=np.float32)


aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)


parameters = aruco.DetectorParameters_create()


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(frame, aruco_dict, parameters=parameters)

    if ids is not None:
        
        frame = aruco.drawDetectedMarkers(frame, corners, ids)

        
        rvecs, tvecs, _ = aruco.estimatePoseSingleMarkers(corners, 0.05, camera_matrix, dist_coeffs)

        
        for i in range(len(ids)):
            aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 0.1)

    
    cv2.imshow('Aruco Marker Detection', frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
