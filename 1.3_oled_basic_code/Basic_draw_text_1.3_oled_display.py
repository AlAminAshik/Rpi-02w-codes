import time
import busio
from board import SCL, SDA
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont


#create I2c interface
i2c = busio.I2C(SCL, SDA)

#create oled class
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3C)

#clear display
oled.fill(0)
oled.show()

#create image buffer
image = Image.new("1", (128, 32))
draw = ImageDraw.Draw(image)

#load font
font = ImageFont.load_default()

#draw text
draw.text((0, 0), "Hello world", font=font, fill=255)

#display image
oled.image(image)
oled.show()