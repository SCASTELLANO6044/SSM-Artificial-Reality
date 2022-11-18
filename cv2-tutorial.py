import cv2
import os
import numpy as np
# import math
# import argparse
# from obj_loader import *

camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

# dir_name = os.getcwd()
# # Load 3D model from OBJ file
# obj = OBJ(os.path.join(dir_name, 'models/fox.obj'), swapyz=True)
#
# def render(img, obj, projection, model, color=False):
#     """
#     Render a loaded obj model into the current video frame
#     """
#     vertices = obj.vertices
#     scale_matrix = np.eye(3) * 3
#     h, w = model.shape
#
#     for face in obj.faces:
#         face_vertices = face[0]
#         points = np.array([vertices[vertex - 1] for vertex in face_vertices])
#         points = np.dot(points, scale_matrix)
#         # render model in the middle of the reference surface. To do so,
#         # model points must be displaced
#         points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
#         dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
#         imgpts = np.int32(dst)
#         if color is False:
#             cv2.fillConvexPoly(img, imgpts, (0, 0, 0))
#         else:
#             color = hex_to_rgb(face[-1])
#             color = color[::-1]  # reverse
#             cv2.fillConvexPoly(img, imgpts, color)
#
#     return img
#
# def hex_to_rgb(hex_color):
#     """
#     Helper function to convert hex strings to RGB
#     """
#     hex_color = hex_color.lstrip('#')
#     h_len = len(hex_color)
#     return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len // 3))

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s == 'image:1':
                    print(s)
                    color = (0, 255, 0)
                    frame = cv2.putText(frame, 'SUBSEA', p[0].astype(int),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    # frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)
    else:
        print('No se puede acceder al vídeo')
        break

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)