import numpy as np
import cv2 as cv

# Callback Function
def nothing(x):
    print(x)
''''''
# for getting perfect threshold
cv.namedWindow('Track Bar')
# To create Track bar
cv.createTrackbar("Th1", 'Track Bar', 0, 255, nothing)
cv.createTrackbar("Th2", 'Track Bar', 0, 255, nothing)

while True:
    img = cv.imread('image/shapes.jpg')
    cv.imshow('Shapes', img)
    imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    th1 = cv.getTrackbarPos('Th1', 'Track Bar')
    th2 = cv.getTrackbarPos('Th2', 'Track Bar')
    _, thresh = cv.threshold(imggray, th1, th2, cv.THRESH_BINARY)  # th1=(103 to 111 any number) , th2=255
    contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    for contour in contours:
        approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
        cv.drawContours(img, [approx], 0, (0, 0, 0), 5)
        x = approx.ravel()[0] + 12
        y = approx.ravel()[1] + 12
        if len(approx) == 3:
            cv.putText(img, "Triangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 4:
            x1, y1, w, h = cv.boundingRect(approx)
            aspectRatio = float(w)/h
            print(aspectRatio)
            if aspectRatio >= 0.95 and aspectRatio <= 1.05:
                cv.putText(img, "Square", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
            else:
                cv.putText(img, "Rectangle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 5:
            cv.putText(img, "Pentagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 6:
            cv.putText(img, "Hexagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 7:
            cv.putText(img, "Heptagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 8:
            cv.putText(img, "Octagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 9:
            cv.putText(img, "Nonagon", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        elif len(approx) == 10:
            cv.putText(img, "Star", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
        else:
            cv.putText(img, "Circle", (x, y), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))

    cv.imshow(' Detected Shapes', img)
    key = cv.waitKey(1)
    if key == 27:
        break
cv.destroyAllWindows()
