import cv2, time

video=cv2.VideoCapture(0)

key = 0
while key != ord('q'):
    # Get frame
    check, frame = video.read()

    # Display image
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

# shutdown camera
video.release()

# Close al widows
cv2.destroyAllWindows()
