import cv2
import numpy as np

image_path = "stego_image.png"
image = cv2.imread(image_path)

if np.any(image[:, :, 0] != image[:, :, 1]):
    print("[INFO] Steganography detected!")
else:
    print("[INFO] No hidden data found."
