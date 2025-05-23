import RPi.GPIO as GPIO #import this allows to control GPIO pins
import time

#GPIO.setmode(GPIO.BOARD) #use physical pin numbering doesnot work for raspberry pi zero 2w
GPIO.setmode(GPIO.BCM) #use physical pin numbering
GPIO.setwarnings(False) #ignore warnings for now

LED = 21

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LED, GPIO.LOW)
    time.sleep(0.5)