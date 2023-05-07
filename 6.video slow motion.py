import cv2

# Open the video file
cap = cv2.VideoCapture('C:/Users/ELCOT/abi/Hani Bday 2022/11111111/VID-20221222-WA0006.mp4')

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Define a factor by which to slow down the video
slow_factor = 2

while(cap.isOpened()):
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if ret == True:
        # Display the frame
        cv2.imshow('Frame',frame)

        # Wait for a small amount of time to slow down the video
        # The time delay is calculated based on the factor by which the video is slowed down
        if cv2.waitKey(int(1000/(slow_factor*fps))) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
