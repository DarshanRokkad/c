# Question 6 : convert image into from one color space to another color space

import cv2

# Read the input color image
image = cv2.imread("baby.jpg")

# Convert BGR to Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original, grayscale, and HSV images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", image_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()