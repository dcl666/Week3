import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
p = GPIO.PWM(11, 128)

GPIO.output(11, GPIO.HIGH)
time.sleep(5)
GPIO.output(11, GPIO.LOW)
