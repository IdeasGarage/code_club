from espeak import espeak
import time

while 1:
    espeak.synth("Hello World")
    time.sleep(2)
