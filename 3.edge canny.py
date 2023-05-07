import cv2
import numpy as np

# Load the image
img = cv2.imread('C:/Users/ELCOT/Downloads/download.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Perform Canny edge detection
edges = cv2.Canny(blur, 100, 200)

# Show the result
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
