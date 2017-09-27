def pytha_finc_c(a, b):
    sum = a**2 + b**2
    return (lambda x: x**(1/2))(sum)


def sqr(x):
    return x**3


print(sqr(5))

print(16**(1/2))

print(float(pytha_finc_c(3, 4)))

import scipy.misc
import numpy as np

# Image size
width = 640
height = 480
channels = 3

# Create an empty image
img = np.zeros((height, width, channels), dtype=np.uint8)

# Draw something (http://stackoverflow.com/a/10032271/562769)
xx, yy = np.mgrid[:height, :width]
circle = (xx - 100) ** 2 + (yy - 100) ** 2

# Set the RGB values
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        r, g, b = circle[y][x], circle[y][x], circle[y][x]
        img[y][x][0] = r
        img[y][x][1] = g
        img[y][x][2] = b

# Display the image
scipy.misc.imshow(img)

# Save the image
scipy.misc.imsave("image.png", img)