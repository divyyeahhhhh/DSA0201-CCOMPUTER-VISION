import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/divya/OneDrive/Documents/COMPUTER VISION/Girl with a Cat.png", cv2.IMREAD_GRAYSCALE)

# Apply the Sobel operator
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1)
edges = cv2.magnitude(dx, dy)

# Threshold the edges
thresh = 100
edges[edges < thresh] = 0
edges[edges >= thresh] = 255

# Display the result
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
