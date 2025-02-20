from Classes.ASCIIArt import ASCIIRenderer
from PIL import Image
#Much inspired by @link https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/
import cv2
def initCamera():
    try:
        return cv2.VideoCapture(0)
    except:
        return cv2.VideoCapture(1)
cam = initCamera()
def img_supplier() -> Image:
    return Image.fromarray(cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2RGB))
#True for background can't render quick enough
renderOb = ASCIIRenderer(img_supplier(),100,False, .6)
# renderOb.displayPicToWindow(700,700)AZ
renderOb.displayVidToWindow(img_supplier,100,1400,900)



