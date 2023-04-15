import cv2
import requests

url = "https://ik.imagekit.io/ikmedia/python-resizing/sunset_SLoRHsWVo.jpg"
r = requests.get(url, allow_redirects=True)

open("sunset.jpg", "wb").write(r.content)

src = "sunset.jpg"
destination = "sunset_resized.jpg"

cv2.imread(src, cv2.IMREAD_UNCHANGED)
cv2.imshow("Original", src)

# Percent by which the image is resized
scale_percent = 60

# Resize the image
height = int(src.shape[0] * scale_percent / 100)
width = int(src.shape[1] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
cv2.waitKey(0)
