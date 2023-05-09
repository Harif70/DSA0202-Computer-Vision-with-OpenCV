import cv2
import numpy as np

# Read input image
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg', 0)

# Define the kernel for the operation
kernel = np.ones((3,3), np.uint8)

# Apply the morphological gradient operation
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Display the result
cv2.imshow('Morphological Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
