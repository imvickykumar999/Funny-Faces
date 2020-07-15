import cv2
import numpy as np
import math
from vcam import vcam,meshGen

img = cv2.imread('vicks.png')
H,W = img.shape[:2]

c1 = vcam(H=H,W=W)
plane = meshGen(H,W)

plane.Z += 20*np.exp(-0.5*((plane.X*1.0/plane.W)/0.1)**2)/(0.1*np.sqrt(2*np.pi))
pts3d = plane.getPlane()

pts2d = c1.project(pts3d)
map_x,map_y = c1.getMaps(pts2d)

output = cv2.remap(img,map_x,map_y,interpolation=cv2.INTER_LINEAR)

cv2.imshow("Funny Mirror",output)
cv2.imshow("Input and output",np.hstack((img,output)))
cv2.waitKey(0)