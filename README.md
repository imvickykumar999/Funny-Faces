# Funny-Faces

Theory

Understanding camera projection matrix
Camera projection matrix (P) provides a mapping between a 3D world coordinate and its corresponding pixel coordinate in an image captured by the respective camera. It is dependent on intrinsic and extrinsic parameters of a camera.

Intrinsic camera parameters: Internal properties of a camera that do not change when translating or rotating the camera in the 3D world coordinate frame.

Focal length (depends on the lens used and mechanical arrangement of camera)
Apperent pixel size (size if one pixel on the image sensor array)
Pricipal point offset (principal point : intersection of the image plane and its normal)
Extrinsic camera parameters: External camera properties that are dependent on the camera pose.

Camera rotation (rotation of camera in the 3D world along all the three axis)
Camera translation (translation of camera in the 3D world)
