from PIL import Image
import requests

url = "https://ik.imagekit.io/ikmedia/python-resizing/sunset_SLoRHsWVo.jpg"
r = requests.get(url, allow_redirects=True)

open("sunset.jpg", "wb").write(r.content)

image = Image.open("sunset.jpg")
print(f"Original Image Size: {image.size}")

sunset_resized = image.resize((300, 300))
sunset_resized.save("sunset_resized.jpg")

print(f"Resized Image Size: {sunset_resized.size}")
