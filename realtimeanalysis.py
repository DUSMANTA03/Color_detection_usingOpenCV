import cv2
from matplotlib import pyplot as plt
cam = cv2.VideoCapture(0)
result, image = cam.read()
if result:
	cv2.imshow("CAPTURED", image)
	cv2.imwrite("CAPTURED.png", image)
	cv2.waitKey(0)
	cv2.destroyWindow("CAPTURED")
else:
	print("No image detected. Please! try again")
def first(imgage):
    img1 = cv2.imread('CAPTURED.png', 0)
    print("Pixels values for image 1 is: ", img1)
    cv2.imshow('Grayscale Image Of CAPTURED', img1)
    histr = cv2.calcHist([img1], [0], None, [256], [0, 256])
    plt.plot(histr)
    plt.show()
first('CAPTURED.png')
