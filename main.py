# put final code into github

# import the necessary packages
import cv2
import numpy as np

# use open cv to read the image and get its values.
img = cv2.imread('use.png', cv2.IMREAD_COLOR)

# Convert to those values to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))

# Apply Hough transform on the blurred image and also pick the min and max size of the circle.
detected_circles = cv2.HoughCircles(gray_blurred,
									cv2.HOUGH_GRADIENT, 1, 20, param1=50,
									param2=30, minRadius=60, maxRadius=500)

# Draw circles that are detected.
if detected_circles is not None:

	# Convert the circle parameters a, b and r to integers.
	detected_circles = np.uint16(np.around(detected_circles))

	for pt in detected_circles[0, :]:
		a, b, r = pt[0], pt[1], pt[2]

		# Draw the circumference of the circle.
		cv2.circle(img, (a, b), r, (255, 0, 0), 10)

		# Draw a middle dot to show the center.
		cv2.circle(img, (a, b), 1, (34, 167, 255), 10)
		cv2.imshow("Detected Circle", img)
		cv2.waitKey(0)