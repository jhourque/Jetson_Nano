import cv2, time

video=cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
video.set(cv2.CAP_PROP_AUTOFOCUS, 255)      # 0 to 255 -> not working. Disabled autofocus with v4l2-ctl -c focus_auto=0
                                            # Then: v4l2-ctl -d /dev/video0 -c focus_absolute=20 
video.set(cv2.CAP_PROP_EXPOSURE, 10)        # not working either -> use v4l2-ctl -d /dev/video0 -c exposure_auto=1
                                            # Then: v4l2-ctl -d /dev/video0 -c exposure_absolute=156 




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
