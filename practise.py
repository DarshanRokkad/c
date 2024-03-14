import cv2
import numpy as np
import math

def rotate2d():
    img = np.zeros((200, 200))
    cv2.rectangle(img, (50, 50), (150,150), 255, -1)
    
    angle = 0
    
    while True:
        img = cv2.warpAffine(img, cv2.getRotationMatrix2D((100, 100), angle, 1), (200, 200))
        
        angle += 1
        
        cv2.imshow('image', img)
        key = cv2.waitKey(30)
        if key == ord('q'):
            break
        
    cv2.destroyAllWindows()

def rotate3d():
    vertics = np.array(
        [
            [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
            [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
        ]
    )
    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]
    angle = 0

    while True:
        
        rotated_matrix = np.array(
            [
                [math.cos(angle), -math.sin(angle), 0],
                [math.sin(angle), math.cos(angle), 0],
                [0, 1, 1]
            ], dtype = np.float32
        )
        rotated_vertics = np.dot(vertics, rotated_matrix)
        projected_vertics = (rotated_vertics[:, :2] * 75 + np.array([300, 300])).astype(int)
        
        img = np.zeros((600, 600, 3))
        for edge in edges:
            pt1 = tuple(projected_vertics[edge[0]])
            pt2 = tuple(projected_vertics[edge[1]])
            cv2.line(img, pt1, pt2, (255, 255, 255), 2)
        
        angle+=0.03
        
        cv2.imshow('image', img)
        key = cv2.waitKey(30)
        if key == ord('q'):
            break

    cv2.destroyAllWindows()
    
    
rotate2d()
rotate3d()