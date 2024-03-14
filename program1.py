# Question 1 : create 2d image

import cv2
import numpy as np

image = np.zeros((500, 500, 3))

# Draw a blue rectangle: image, top-left corner, bottom-right corner, color (BGR), thickness
cv2.rectangle(image, (100, 100), (300, 300), (0, 255, 0), -1)

# Display the image
cv2.imshow("Created Image", image)
cv2.waitKey(0)  # Wait for a key press to close

cv2.destroyAllWindows()