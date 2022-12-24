import cv2
import numpy as np

panel = np.zeros([100, 70, 3], np.uint8)
cv2.namedWindow("panel")

def nothing(x):
    print(x)
    pass

cv2.createTrackbar("L - h", "panel", 0, 255, nothing)
cv2.createTrackbar("U - h", "panel", 179, 179, nothing)

cv2.createTrackbar("L - s", "panel", 0, 255, nothing)
cv2.createTrackbar("U - s", "panel", 255, 255, nothing)

cv2.createTrackbar("L - v", "panel", 0, 255, nothing)
cv2.createTrackbar("U - v", "panel", 255, 255, nothing)

cap = cv2.VideoCapture("solution_85.jpg")

while True:
    img = cv2.imread("solution_85.jpg")

    width = 500
    height = 500  # keep original height
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    print(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L - h", "panel")
    u_h = cv2.getTrackbarPos("U - h", "panel")
    l_s = cv2.getTrackbarPos("L - s", "panel")
    u_s = cv2.getTrackbarPos("U - s", "panel")
    l_v = cv2.getTrackbarPos("L - v", "panel")
    u_v = cv2.getTrackbarPos("U - v", "panel")

    low = np.array([l_h, l_s, l_v])
    high = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, low, high)
    mask_inv = cv2.bitwise_not(mask)

    fg = cv2.bitwise_and(img, img, mask=mask)
    bg = cv2.bitwise_and(img, img, mask=mask_inv)

    cv2.imshow("fg", fg)
    cv2.imshow("bg", bg)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
