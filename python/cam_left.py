import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)			#dies beeinflusst wahrscheinlich den speed. evtl ändern

try:
        while True:
                p.ChangeDutyCycle(-1) # unsicher ob richtige zahl      später zahl senken und mehrfach ausführen solange taste gedrückt wird.
               # time.sleep(1) # sleep 1 second
             
			  # if p.dutyCycle == 7.5 :							#evtl falsch?
			  # p.stop()
			  # break
			   
except KeyboardInterrupt:
		p.stop()
        break    #muss später wahrscheinlch verändert werden