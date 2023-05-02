import cv2
 

path = r"C:/Users/Welcome/OneDrive/Pictures/Saved Pictures/cat.jpeg"
 
src = cv2.imread(path)
 
window_name = 'Image'

image = cv2.rotate(src, cv2.ROTATE_180)
 
# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
