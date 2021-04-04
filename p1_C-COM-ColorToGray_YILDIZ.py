# Import Libraries
from PIL import Image
import matplotlib.pyplot as plt

# Get Image Input
path = input("Enter the exact path to the image: ")

# Size of the Image
img = Image.open(path)
width = img.size[0]
height = img.size[1]

# Get the Pixels
def pixels(img, x, y):
    if x > width or y > height:
      return None

    pixel = img.getpixel((x, y))
    return pixel

# Convert RGB Pixels to Gray
def rgb2gray(img):
  gray_scale = img
  pixel = gray_scale.load()

  for x in range (0, width):
    for y in range (0, height):
      rgbpixels = pixels(img, x, y)

      red = rgbpixels[0]
      green = rgbpixels[1]
      blue = rgbpixels[2]

      gray = (red*0.299 + green*0.587 + blue*0.114)

      pixel[x,y] = (int(gray), int(gray), int(gray))

  return gray_scale

  
# Display Both the Original and the Gray Image  
image1 = plt.figure(1)
plt.imshow(img)

image2 = plt.figure(2)
grayImage = rgb2gray(img)
plt.imshow(grayImage)

plt.show()
