# Question 5 : erosion and dilation

import cv2

# Read the input color image
image = cv2.imread("girl.webp")
image = cv2.resize(image, None, fx=0.3, fy=0.3)

# Erosion
eroded_image = cv2.erode(image, (3, 3), iterations=5)
# Dilation
dilated_image = cv2.dilate(image, (3, 3), iterations=5)

# Display the original, eroded, and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded_image)
cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)

cv2.destroyAllWindows()