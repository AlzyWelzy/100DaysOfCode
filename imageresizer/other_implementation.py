import cv2
import requests

url = "https://ik.imagekit.io/ikmedia/python-resizing/sunset_SLoRHsWVo.jpg"
r = requests.get(url, allow_redirects=True)

open("sunset.jpg", "wb").write(r.content)

cv2.imshow("Original Image", cv2.imread("sunset.jpg"))
