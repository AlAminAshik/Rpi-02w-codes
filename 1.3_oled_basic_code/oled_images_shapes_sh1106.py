# This code utilizes the luma library to display on oled display
# steps to run this code
# we need to get inside virtual environment
# if already created, go inside the env folder and type "source bin/activate"
# once inside, go back (cd ..) and type "python3 oled_images_shapes_sh1106.py"
# if error persists check for i2c connected device by typing "sudo i2cdetect -y 1"
# Note: installing any libary using "pip" requires you to stay inside the virtual environment
# Note: This is interchangable with ssd1306 oled display

from luma.core.interface.serial import i2c		#for first timer install "pip install luma.oled"
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont		#for first timer install "pip install pillow"
import time										#for adding delay

# initialize i2c display
device = sh1106(i2c(port=1, address=0x3c)) 		#displaytype(primary i2c port and address) 

# load fonts
fontSmall = ImageFont.load_default()
fontLarge = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",20)

i = 0
direction = 1

while True:
    # create blank canvas
    image = Image.new("1", device.size)
    draw = ImageDraw.Draw(image)
    
    # Draw shapes
    draw.rectangle((0,0,127,63), outline=255, fill=0)
    draw.ellipse((5,5,25,25), outline=255, fill=0)

    #Draw texts (texts should be after shapes)
    draw.text((30,8), "Small text", font=fontSmall, fill=255)
    draw.text((10,38), "Big text", font=fontLarge, fill=255)
    
    #calculate line positions
    x1 = 32-i
    x2 = 32+i
    x3 = 96-i
    x4 = 96+i
    
    #draw two bouncing horizontal lines
    draw.line((x1,32,x2,32), fill=255)
    draw.line((x3,32,x4,32), fill=255)
    
    #Display image
    device.display(image)
    
    #update motion
    i += direction
    if i>=32 or i<=0:
        direction *= -1	#reverse direction
        
    time.sleep(0.0001)
