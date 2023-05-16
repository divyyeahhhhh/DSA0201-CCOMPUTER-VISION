import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/divya/Downloads/Girl with a Cat.png", cv2.IMREAD_GRAYSCALE)

# Create a structuring element
kernel = np.ones((5,5), np.uint8)

# Apply closing
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# Display the result
cv2.imshow("Original", img)
cv2.imshow("opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
