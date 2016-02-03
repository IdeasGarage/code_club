import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT)
while True:
    input_state = GPIO.input(12)
    
    if input_state == False:
        GPIO.output(7, True)
        time.sleep(0.2)
        GPIO.output(7, False)

