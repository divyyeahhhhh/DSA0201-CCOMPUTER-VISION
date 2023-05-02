# import necessary libraries

import cv2
import numpy as np

# Turn on Laptop's webcam
cap = cv2.VideoCapture("C:/Users/Welcome/Downloads/pexels-pixabay-855029-1920x1080-60fps.mp4")

while True:
	
	ret, frame = cap.read()

	# Locate points of the documents
	# or object which you want to transform
	pts1 = np.float32([[200,300], [5, 2],
					[0, 4], [6, 0]])
	pts2 = np.float32([[0, 0], [4, 0],
					[0, 1], [4, 6]])
	
	# Apply Perspective Transform Algorithm
	matrix = cv2.getPerspectiveTransform(pts1, pts2)
	result = cv2.warpPerspective(frame, matrix, (0, 0))
	
	# Wrap the transformed image
	cv2.imshow('frame', frame) # Initial Capture
	cv2.imshow('frame1', result) # Transformed Capture

	if cv2.waitKey(24) == 27:
		break

cap.release()
cv2.destroyAllWindows()
