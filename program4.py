# Question 4 : 2d and 3d image rotating

import cv2
import math
import numpy as np

def continuously_rotate_2d():
    img_2d = np.zeros((200, 200))
    cv2.rectangle(img_2d, (50, 50), (150, 150), 255, -1)
    
    angle = 0
    while True:
        # Calculate the rotation matrix
        rm = cv2.getRotationMatrix2D((100, 100), angle, 1)
        img = cv2.warpAffine(img_2d, rm, (200, 200))
        
        angle+=1
        
        cv2.imshow('Rotating Square', img)        
        key = cv2.waitKey(30)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()

def continuously_rotate_3d():
    # Define cube vertices in 3D space
    vertices = np.array([[-1, -1, -1],
                         [1, -1, -1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, 1],
                         [-1, 1, 1]], dtype=np.float32)

    # Define cube edges
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    # Create a rotation matrix
    angle = 0

    while True:
           rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                       [math.sin(angle), math.cos(angle), 0],
                                       [0, 1, 1]], dtype=np.float32)

           # Rotate the cube vertices in 3D space
           rotated_vertices = np.dot(vertices, rotation_matrix)

           # Project the 3D points to 2D
           projected_vertices = (rotated_vertices[:, :2] * 75 + np.array([300, 300])).astype(int)

           # Create a black image
           frame = np.ones((600, 600, 3)) * (0, 0, 0)

           # Draw cube edges
           for edge in edges:
               pt1 = tuple(projected_vertices[edge[0]])
               pt2 = tuple(projected_vertices[edge[1]])
               cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

           # Display the frame
           cv2.imshow("Rotating 3D Cube", frame)

           # Wait for a moment and update the angle
           key = cv2.waitKey(30)
           if key == ord('q'):
                break
            
           angle += 0.03  # Adjusted rotation speed

    # Release the window
    cv2.destroyAllWindows()

continuously_rotate_2d()
continuously_rotate_3d()