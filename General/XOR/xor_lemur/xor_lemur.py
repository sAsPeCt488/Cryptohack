import numpy as np
from PIL import Image

# Open images
flag  = Image.open("flag.png")
lemur  = Image.open("lemur.png")

# Convert to NumPy arrays
flagnp = np.array(flag)*255
lemurnp = np.array(lemur)*255

# XOR 
result = np.bitwise_xor(flagnp, lemurnp).astype(np.uint8)

# Save
Image.fromarray(result).save('result.png')
