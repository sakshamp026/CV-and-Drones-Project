import cv2
import numpy as np

# Read the distorted image
image = cv2.imread("photos\Chess_Board.jpg")

# Preprocess the image
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
gray = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2GRAY)

# Find the corners of the chessboard in the image
corners_found, corners = cv2.findChessboardCorners(gray, (7, 7), None)

if corners_found:
    # Refine corner positions
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

    # Define the object points (coordinates of the chessboard corners in 3D space)
    obj_points = np.zeros((7 * 7, 3), np.float32)
    obj_points[:, :2] = np.mgrid[0:7, 0:7].T.reshape(-1, 2)

    # Calibrate the camera using the chessboard corners
    obj_points_list = [obj_points]
    img_points_list = [corners]
    camera_matrix, distortion_coefficients, _, _, _ = cv2.calibrateCamera(
        obj_points_list, img_points_list, gray.shape[::-1], None, None
    )

    # Undistort the image using the camera calibration results
    undistorted_image = cv2.undistort(image, camera_matrix, distortion_coefficients, None, camera_matrix)

    # Save the undistorted image
    cv2.imwrite('undistorted_chessboard.png', undistorted_image)

    # Display the undistorted image
    cv2.imshow('Undistorted Image', undistorted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Chessboard corners not found in the image.")
