# This code utilizes the luma library to display on oled display
# steps to run this code
# we need to get inside virtual environment
# if already created, go inside the env folder and type "source bin/activate"
# once inside, go back (cd ..) and type "python3 oled_hello_sh1106.py"
# if error persists check for i2c connected device by typing "sudo i2cdetect -y 1"
# Note: installing any libary using "pip" requires you to stay inside the virtual environment
# Note: This is interchangable with ssd1306 oled display

from luma.core.interface.serial import i2c		#pip install luma.oled
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont		#pip install pillow
import time										#for adding delay

# initialize i2c display
device = sh1106(i2c(port=1, address=0x3c)) 		#displaytype(primary i2c port and address) 

# create blank image
image = Image.new("1", device.size)
draw = ImageDraw.Draw(image)

# load default font
font = ImageFont.load_default()

#Draw text
draw.text((20,30), "hello world", font=font, fill=255)

#Display image
device.display(image)

#show for 5 seconds
time.sleep(5)