
# coding: utf-8

# In[ ]:

import matplotlib.pyplot as plt
import cv2
import numpy as np
def flowVisualUseColor(flow):
    hsv = np.zeros([flow.shape[0],flow.shape[1],3], dtype=np.uint8)
    hsv[:, :, 0] = 255
    hsv[:, :, 1] = 255
    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    plt.figure()
    # plt.axis('off')
    plt.imshow(rgb)
    plt.show()

