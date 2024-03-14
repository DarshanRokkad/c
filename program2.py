# Question 2 : create 3d image

import cv2
import numpy as np
import math

vertices = np.array([[-1, -1, -1],
                     [1, -1, -1],
                     [1, 1, -1],
                     [-1, 1, -1],
                     [-1, -1, 1],
                     [1, -1, 1],
                     [1, 1, 1],
                     [-1, 1, 1]])

edges = [(0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)]

angle = 0

while True:
        rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                   [math.sin(angle), math.cos(angle), 0],
                                   [0, 1, 1]], dtype=np.float32)
       
        # Rotate the cube vertices in 3D space
        rotated_vertices = np.dot(vertices, rotation_matrix)
       
        # Project the 3D points to 2D
        projected_vertices = (rotated_vertices[:, :2] * 75 + np.array([300, 300])).astype(int)
       
        img = np.zeros((600, 600, 3))

        for edge in edges:
            pt1 = tuple(projected_vertices[edge[0]])
            pt2 = tuple(projected_vertices[edge[1]])
            cv2.line(img, pt1, pt2, (255, 255, 255), 2)
        
        angle += 0.03
 
        cv2.imshow("Rotating 3D Cube", img)
        key = cv2.waitKey(30)
        if key == ord('q'):
             break

cv2.destroyAllWindows()