# Load opencv
import cv2

# Load the images which you need for image processing
image01 = cv2.imread('../directory/image01.png', 0)
image02 = cv2.imread('../directory/image02.png', 0)

# Intilaize SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# Detect the important keypoints and compute descriptions for both choosen images
kp1, des1 = sift.detectAndCompute(image01, None)
kp2, des2 = sift.detectAndCompute(image02, None)

# print the number of keypoints for each image
print("Number of keypoint in image 1: ", len(kp1))
print("Number of keypoint in image 2: ", len(kp2))

# Display the keypoints on the images
image01_kp = cv2.drawKeypoints(image01, kp1, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
IMAGE02_KP = cv2.drawKeypoints(image02, kp2, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Now time to show the results
cv2.imshow('Image01 with keypoints', image01_kp)
cv2.imshow('Image02 with keypoints', image02_kp)
cv2.waitkey(0)
cv2.destoryAllWindow()
