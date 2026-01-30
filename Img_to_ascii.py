import cv2
import sys

image_path = r"c:\Users\kevin\OneDrive\Desktop\pep\cristiano.jpg" #Enter the path to your Image


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found or path is incorrect.")
    sys.exit()


height, width = image.shape
new_width = 150
new_height = int((height / width) * new_width)
image = cv2.resize(image, (new_width, new_height))


ascii_chars = "@#S%?*+;:,."

ascii_image = ""


for i in range(new_height):
    for j in range(new_width):
        pixel = image[i][j]

        if pixel < 25:
            ascii_image += ascii_chars[0]
        elif pixel < 50:
            ascii_image += ascii_chars[1]
        elif pixel < 75:
            ascii_image += ascii_chars[2]
        elif pixel < 100:
            ascii_image += ascii_chars[3]
        elif pixel < 125:
            ascii_image += ascii_chars[4]
        elif pixel < 150:
            ascii_image += ascii_chars[5]
        elif pixel < 175:
            ascii_image += ascii_chars[6]
        elif pixel < 200:
            ascii_image += ascii_chars[7]
        elif pixel < 225:
            ascii_image += ascii_chars[8]
        else:
            ascii_image += ascii_chars[9]

    ascii_image += "\n"


print(ascii_image)


output_file = r"c:\Users\kevin\OneDrive\Desktop\pep\for_loop.txt"
with open(output_file, "w") as file:
    file.write(ascii_image)

print("\nASCII image successfully saved as for_loop.txt")

