import cv2
import numpy as np
import math

vertices = np.array(
    [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1],
    ],
    dtype=np.float32,
)

edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
]

faces = [
            (0, 1, 2, 3),
            (4, 5, 6, 7),
            (0, 1, 5, 4),
            (2, 3, 7, 6),
            (1, 2, 6, 5),
            (0, 3, 7, 4),
        ]

colors = [
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
]

angle_x, angle_y, angle_z = 0, 0, 0
while True:
    rotation_matrix_x = np.array(
        [
            [1, 0, 0],
            [0, math.cos(angle_x), -math.sin(angle_x)],
            [0, math.sin(angle_x), math.cos(angle_x)],
        ],
        dtype=np.float32,
    )
    rotation_matrix_y = np.array(
        [
            [math.cos(angle_y), 0, math.sin(angle_y)],
            [0, 1, 0],
            [-math.sin(angle_y), 0, math.cos(angle_y)],
        ],
        dtype=np.float32,
    )
    rotation_matrix_z = np.array(
        [
            [math.cos(angle_z), -math.sin(angle_z), 0],
            [math.sin(angle_z), math.cos(angle_z), 0],
            [0, 0, 1],
        ],
        dtype=np.float32,
    )
    rotated_vertices = np.dot(vertices, rotation_matrix_x)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_y)
    rotated_vertices = np.dot(rotated_vertices, rotation_matrix_z)

    projected_vertices = (
        rotated_vertices[:, :2] * 100 + np.array([250, 250])
    ).astype(int)

    image = np.zeros((500, 500, 3))

    for i, face in enumerate(faces):
        cv2.fillPoly(image, [projected_vertices[face, :]], color=colors[i])

    for edge in edges:
        pt1 = tuple(projected_vertices[edge[0]])
        pt2 = tuple(projected_vertices[edge[1]])
        cv2.line(image, pt1, pt2, (255, 255, 255), 2)

    cv2.imshow("Cube", image)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("x"):
        angle_x += 0.02
    elif key == ord("y"):
        angle_y += 0.02
    elif key == ord("z"):
        angle_z += 0.02

cv2.destroyAllWindows()