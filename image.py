# to load the library from open cv
import cv2

# Load image to display
img = cv2.imread("schinchan.jpg")

# Display original image
cv2.imshow("Image", img)

# Converting  the original image to gray scale
ch = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Displaying the GrayScale image 
cv2.imshow("Gray Schinchan", ch)

# Resizing the image 
re = cv2.resize(img,(300,300))
cv2.imshow("Resize", re)

# Shaping of image
h, w = img.shape[:2] # use to find the height and width of the image

center = (w // 2, h // 2) # use to find the center of the image

mid = cv2.getRotationMatrix2D(center, 90, 1.0) # use to rotate the image in 90 degree
rotated = cv2.warpAffine(img, mid, (w,h))

cv2.imshow("Rotate image", rotated)

# to flip the image upside down
flip_img = cv2.flip(img, 0)
cv2.imshow("flip image", flip_img)

# to crop the image
crop = img[100:300, 150:350]
cv2.imshow("Cropped", crop)

# to draw a line on image
# to draw a line on image
pt1 = (50, 100)
pt2 = (300, 100)
color = (0, 0, 255)   
thickness = 4
cv2.line(img, pt1, pt2, color, thickness)
cv2.imshow("Draw line", img)
# Freezing the screen the user press any key
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
