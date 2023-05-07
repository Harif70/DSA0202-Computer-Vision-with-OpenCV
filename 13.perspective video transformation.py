import cv2
import numpy as np

# Load the video
cap = cv2.VideoCapture("C:/Users/ELCOT/abi/Hani Bday 2022/11111111/VID-20221222-WA0006.mp4")

# Define the source and destination points for perspective transformation
src = np.float32([[207, 236], [560, 236], [0, 720], [960, 720]])
dst = np.float32([[0, 0], [960, 0], [0, 720], [960, 720]])

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    
    if ret:
        # Perform perspective transformation on the frame
        M = cv2.getPerspectiveTransform(src, dst)
        warped = cv2.warpPerspective(frame, M, (960, 720))
        
        # Display the transformed frame
        cv2.imshow("Perspective Transformed Frame", warped)
        
        # Press 'q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
