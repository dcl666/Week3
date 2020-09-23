import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 128) #通道为 11 频率为 128Hz

p.start(0) #启动PWM

try:

   while 1:

       for dc in range(0, 101, 5):

           p.ChangeDutyCycle(dc)

           time.sleep(0.1)

       for dc in range(100, -1, -5):

           p.ChangeDutyCycle(dc)

           time.sleep(0.1)
 
except KeyboardInterrupt: #设置按CTRL+C终止（inter i是大写I）

    pass

p.stop() #停止PWM

GPIO.cleanup()