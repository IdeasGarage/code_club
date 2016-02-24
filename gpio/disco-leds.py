import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(31,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
      GPIO.output(7,True)
      time.sleep(0.1)
      GPIO.output(7,False)
      time.sleep(0.1)
      GPIO.output(11,True)
      time.sleep(0.1)
      GPIO.output(11,False)
      time.sleep(0.1)
      GPIO.output(15,True)
      time.sleep(0.1)
      GPIO.output(15,False)
      time.sleep(0.1)
      GPIO.output(35,True)
      time.sleep(0.1)
      GPIO.output(35,False)
      time.sleep(0.1)                                                                                                                                                                                                                
      
