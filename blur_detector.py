import argparse
import cv2

def laplacian_variance(image):
    
    return cv2.Laplacian(image, cv2.CV_64F).var()

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "path to image")
ap.add_argument("-t", "--threshold", type = float, default = 100., help = "Value that seperates blurry and no-blurry images")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
var = laplacian_variance(gray)
text = "Not Blurry"

if var < args["threshold"]:
    text = "Blurry"
    
cv2.putText(image, "{}: {:.2f}".format(text, var), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

cv2.imshow("Image", image)
cv2.waitKey(0)
