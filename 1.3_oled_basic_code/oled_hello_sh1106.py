from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import time

serial = i2c(port=1, address=0x3c)
device = sh1106(serial)

image = Image.new("1", device.size)
draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

draw.rectangle(device.bounding_box, outline=0, fill=0)

draw.text((20,30), "hello", font=font, fill=255)

device.display(image)

time.sleep(5)