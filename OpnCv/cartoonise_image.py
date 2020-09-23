import cv2
import numpy as np
num_down = 2
num_bilateral = 7

img_rgb = cv2.imread('sample0.jpg')
#print(img_rgb.shape) # Dimensions

img_rgb = cv2.resize(img_rgb, (800, 800))

img_color = img_rgb
for _ in range(num_down):
    img_color = cv2.pyrDown(img_color)

for _ in range(num_bilateral):
    img_color = cv2.bilateralFilter(img_color, d=6, sigmaColor=6, sigmaSpace=9)


for _ in range(num_down):
    img_color = cv2.pyrUp(img_color)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY,
                                  blockSize=9,
                                  C=3)

img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)                                  
img_cartoon = cv2.bitwise_and(img_color, img_edge)



stack = np.hstack([img_rgb, img_cartoon])

cv2.imshow('Stacked Images',stack)
cv2.imwrite('result0.jpg', stack)