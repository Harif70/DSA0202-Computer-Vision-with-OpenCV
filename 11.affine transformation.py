import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/ELCOT/Downloads/download.jpg")

# Define the affine transformation matrix
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 50], [0, 1, -30]])

# Apply the affine transformation to the image
affine_img = cv2.warpAffine(img, M, (cols, rows))

# Display the original and transformed images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
