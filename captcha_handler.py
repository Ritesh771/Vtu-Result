from PIL import Image
from io import BytesIO
import pytesseract
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

os.environ['TESSDATA_PREFIX'] = resource_path('Tesseract-OCR/tessdata')
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


class CaptchaHandler:
    pixel_range = [(i, i, i) for i in range(100, 160)]

    def get_captcha_from_image(self, target_image):
        image_data = BytesIO(target_image)

        image = Image.open(image_data)
        width, height = image.size

        white_image = Image.new("RGB", (width, height), "white")

        for x in range(width):
            for y in range(height):
                pixel = image.getpixel((x, y))

                if pixel in self.pixel_range:
                    white_image.putpixel((x, y), pixel)

        return pytesseract.image_to_string(white_image).strip()