# Image to ASCII Art Converter (Python + OpenCV)

This project converts a grayscale image into **ASCII art** using **Python and OpenCV**, mapping pixel intensity values to ASCII characters and saving the output as a text file.

**Unique Feature:**  
Unlike many similar projects, this implementation **does NOT use the PIL (Pillow) library**.  
Instead, it relies entirely on **OpenCV** and **basic nested for-loops**, making it lightweight, beginner-friendly, and ideal for understanding low-level image processing logic.

---

##  Features

- Converts images into ASCII art using grayscale pixel values  
- Uses **OpenCV (`cv2`) only** — no PIL/Pillow dependency  
- ASCII mapping implemented using **explicit conditional logic**
- Output displayed in the terminal
- ASCII art saved as a `.txt` file
- Simple and readable code structure

---

##  How It Works

1. The image is read in **grayscale mode** using OpenCV.
2. The image is resized to maintain aspect ratio.
3. Each pixel value (0–255) is mapped to a specific ASCII character.
4. Nested `for` loops traverse the image pixel by pixel.
5. Characters are appended row-wise to form ASCII art.
6. The final ASCII output is:
   - Printed to the console
   - Written to a text file (`for_loop.txt`)

---

##  ASCII Mapping Used

```text
Dark → Light
@ # S % ? * + ; : , .
