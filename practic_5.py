from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
import requests
from io import BytesIO
from PIL import Image

url = 'https://api.selcdn.ru/v1/SEL_72086/prodLMS/files/share/image13_oUYSP3p.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

img_array = np.array(img)

print(img_array.shape)
print(img_array.dtype)

if img_array.shape[-1] == 4:
    img_array = img_array[..., :3]

def replace_color(img, old_color, new_color, tolerance=50):
    r, g, b = old_color
    lower_bound = np.array([r - tolerance, g - tolerance, b - tolerance])
    upper_bound = np.array([r + tolerance, g + tolerance, b + tolerance])
    mask = np.all(np.logical_and(img >= lower_bound, img <= upper_bound), axis=-1)
    img[mask] = new_color
    return img

blue_color = [0, 0, 255]  # RGB для синего
white_color = [255, 255, 255]   # RGB для черного
red_color = [255, 0, 0]   # RGB для красного
green_color = [0, 200, 0] # RGB для зеленого

img_array = replace_color(img_array, blue_color, red_color, tolerance=100)

img_array = replace_color(img_array, white_color, green_color, tolerance=100)

plt.imshow(img_array)
plt.axis('off')
plt.title("Измененное изображение")
plt.show()