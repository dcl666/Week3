import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
def dim()
red led = GPIO.PWM(12, 100)
red led.start(0)
pause time = 0.010
for i in range(0, 100 + 1):
    red led.ChangeDutyCycle(i)
time.sleep(pause time)
for i in range(100, -1, -1):
    red led.ChangeDutyCycle(i)
    time.sleep(pause time)
    GPIO.cleanup()
    dim()
    