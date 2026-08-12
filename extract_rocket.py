from PIL import Image
import numpy as np

# Load the image
img_path = r"C:\Users\rafas\.gemini\antigravity-ide\brain\40601238-bda2-4ce6-8415-8cb1c59fc40e\media__1786500703698.png"
img = Image.open(img_path).convert("RGBA")
data = np.array(img)

# The image has a white rocket and text on an orange background.
# We want to extract only the white rocket. 
# The rocket is in the top part of the image, text is in the bottom.
height, width = data.shape[0], data.shape[1]

# Create a new transparent image data array
new_data = np.zeros((height, width, 4), dtype=np.uint8)

# Find white pixels (R>200, G>200, B>200)
# And limit to the top 65% of the image to exclude the YUPI text
white_mask = (data[:, :, 0] > 200) & (data[:, :, 1] > 200) & (data[:, :, 2] > 200)

for y in range(height):
    for x in range(width):
        if y < height * 0.65 and white_mask[y, x]:
            # Set to brand orange color #EE6900 (238, 105, 0)
            new_data[y, x] = [238, 105, 0, 255]
        else:
            # Transparent
            new_data[y, x] = [0, 0, 0, 0]

# Convert back to image
new_img = Image.fromarray(new_data, "RGBA")

# Crop the bounding box of the non-transparent pixels
bbox = new_img.getbbox()
if bbox:
    new_img = new_img.crop(bbox)

# Save to the images folder
new_img.save("images/logo_foguete.png")
print("Rocket extracted successfully!")
