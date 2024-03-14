# Question 7 : triangle with centroid

import cv2
import numpy as np

def calculateCentroid(val):
    x = int((val[0][0] + val[1][0] + val[2][0]) / 3)
    y = int((val[0][1] + val[1][1] + val[2][1]) / 3)
    return x, y

img = np.zeros((600, 600, 3))
triangleVertices = np.array([[250, 100], [100, 400], [400, 400]])
triangleColor = (255, 0, 0)

while True:
    cv2.fillPoly(img, [triangleVertices.reshape(-1, 1, 2)], triangleColor)
    cv2.circle(img, calculateCentroid(triangleVertices), 5, (255, 255, 255), -1)
    
    cv2.imshow("centroid", img)
    
    key = cv2.waitKey(0)
    
    if key == ord("r"):
        triangleColor = (0, 0, 255)
    elif key == ord("g"):
        triangleColor = (0, 255, 0)
    elif key == ord("b"):
        triangleColor = (255, 0, 0)
        
    if key == ord("q"):
        break

cv2.destroyAllWindows()