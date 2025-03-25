from PIL import Image
from PIL.ExifTags import TAGS

image_path = "image.jpg"
image = Image.open(image_path)
exif_data = image._getexif()

if exif_data:
    for tag, value in exif_data.items():
        print(f"{TAGS.get(tag, tag)}: {value}"
