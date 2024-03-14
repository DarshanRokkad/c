# Question 3 : 2d and 3d image resizing

import cv2
import numpy as np
import math

circle_radius = cube_size = 100
angle = 0

# Create a resizable window
cv2.namedWindow("Resizable 2D and 3D Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Resizable 2D and 3D Images", 400, 400)

# Callback function for trackbar changes
def on_size_change(value):
    global circle_radius, cube_size
    circle_radius = cube_size = value

# Create a trackbar for resizing
cv2.createTrackbar("Size", "Resizable 2D and 3D Images", cube_size, 200, on_size_change)

while True:
    
    # Resize 2D Image (Circle)
    img_2d = np.zeros((300, 300, 3))
    cv2.circle(img_2d, (150, 150), circle_radius, (255, 255, 255), -1)
    cv2.imshow("Resizable 2D Image", img_2d)

    # Resize 3D Image (Rotate Cube)
    vertices = np.array([[-1, -1, -1],
                         [1, -1, -1],
                         [1, 1, -1],
                         [-1, 1, -1],
                         [-1, -1, 1],
                         [1, -1, 1],
                         [1, 1, 1],
                         [-1, 1, 1]], dtype=np.float32)  
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)]
    rotation_matrix = np.array([[math.cos(angle), -math.sin(angle), 0],
                                [math.sin(angle), math.cos(angle), 0],
                                [0, 1, 1]], dtype=np.float32)
    rotated_vertices = np.dot(vertices, rotation_matrix)
    projected_vertices = (rotated_vertices[:, :2] * cube_size + np.array([200, 200])).astype(int)
    frame = np.zeros((400, 400, 3), dtype=np.uint8)
    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (0, 255, 0), 2)
    cv2.imshow("Resizable 3D Image", frame)
    angle += 0.02

    key = cv2.waitKey(30)
    if key == ord('q'):
        break

cv2.destroyAllWindows()