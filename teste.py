import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# Converting to grayscale
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur
def blur(img):
    blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)

show = blur(img)

cv.waitKey(0)