import cv2
import numpy as np
import math


video = cv2.VideoCapture(0)

maxSlider = 10
minLength = 5
maxGap = 10
theta = 0

while True:
    # Capture the video frame
    ret, frame = video.read()
    # Convert to Gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Blur
    b_width = 5
    b_height = 5
    blurred = cv2.GaussianBlur(gray, (b_width, b_height), 0)
    # Canny edge detection
    t1 = 80
    t2 = 80
    edges = cv2.Canny(blurred, t1, t2)
    # Hough
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, maxSlider, minLength, maxGap)
    if lines is not None:
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                # draw line in image using cv2.line function.
                cv2.line(blurred, (x1, y1), (x2, y2), (255, 255, 0), 3)
                theta = theta + math.atan2((y2 - y1), (x2 - x1))
                # print(theta)
        threshold = 5
        if theta > threshold:
            print("Go left")
        if theta < -threshold:
            print("Go right")
        if abs(theta) < threshold:
            print("Go straight")
        theta = 0

    cv2.imshow("Blur", blurred)
    cv2.imshow("Edges", edges)

    if cv2.waitKey(1) & 0xff == ord('q'):  # 1 is the time in ms
        break
# After the loop release the cap object
video.release()
# Destroy all the windows
cv2.destroyAllWindows()