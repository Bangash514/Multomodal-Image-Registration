# Opencv library
import cv2

# Read the images need to be used
image01 = cv2.imread('Directory/image01.png')
image02 = cv2.imread('Directory/image02.png')

# Now we need to intiliaze SIFT detector
sift = cv2.SIFT_create()

# Now we need to detect the all matched keypoint and then compute their descriptors
kp1, des1 = sift.detect&Compute(image01, None)
kp2, des2 = sift.detect&Compute(image02, None)

# Match keypoint between the two images
bf = cv2.BFMatcher()
matches = bf.match(des1,des2)

# Sort matches by distance
matches = sorted(matches, key = lambda x:x.distance)

# Draw your desire matches points
image_matches = cv2.drawMatches(image01, kp1, kp2, matches[:10], None, flags = 2)

# Now its time to display the output result
cv2.imshow('Matches', image_matches)
cv2.waitkey()
