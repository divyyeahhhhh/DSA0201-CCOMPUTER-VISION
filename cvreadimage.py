import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "C:/Users/Welcome/OneDrive/Pictures/Saved Pictures/cat.jpeg"
img =cv2.imread(path)

cv2.imshow("Lena",img)
cv2.waitkey(0)
