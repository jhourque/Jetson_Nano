import cv2, time

video=cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

key = 0
while key != ord('q'):
    # Get frame
    check, frame = video.read()

    edges = cv2.Canny(frame,100,200)

    # Display image
    cv2.imshow("Edges", edges)

    key = cv2.waitKey(1)

# shutdown camera
video.release()

# Close al widows
cv2.destroyAllWindows()
