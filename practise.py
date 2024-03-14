import cv2
import numpy as np

image = np.zeros((500, 500, 3), dtype=np.uint8)

triangle_vertices = np.array([[250, 50], [50, 450], [450, 450]], dtype=np.int32)

cv2.polylines(image, [triangle_vertices], isClosed=True, color=(0, 0, 255), thickness=2)

centroid = np.mean(triangle_vertices, axis=0, dtype=np.int32)

cv2.circle(image, tuple(centroid), radius=2, color=(0, 255, 0), thickness=-1)

cv2.imshow("Triangle", image)

def change_color(event,a,b,c,d):
    global image
    if event==cv2.EVENT_LBUTTONDOWN:
        color_n=np.random.randint(0,266,size=3).tolist()
        cv2.fillPoly(image,[triangle_vertices],color=color_n)
        cv2.circle(image, tuple(centroid), radius=2, color=(0, 255, 0), thickness=-1)
        cv2.imshow("Triangle", image)
cv2.setMouseCallback("Triangle",change_color)

while True:
    key=cv2.waitKey(10) & 0xFF
    if key==ord('q'):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()