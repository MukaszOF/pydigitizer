import cv2
import pytesseract

img = cv2.imread("Screenshot_1.png")
config = r'--oem 3 --psm 6'

pytesseract.pytesseract.tesseract_cmd = "D:\-IMPORTANTE\-Python Librarys\Tesseract-OSR Python\Tesseract.exe"
resultado = pytesseract.image_to_string(img,config=config)
print(resultado)