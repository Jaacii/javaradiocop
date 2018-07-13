import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12,50)

p.start(0)
p.ChangeDutyCycle(0)

dir = input('0 - left, 1 - right: ')

def servo_left():
	p.ChangeDutyCycle(2.5)
	time.sleep(0.1)
	return

,def servo_right():
	p.ChangeDutyCycle(10)
	time.sleep(0.1)
	return

try:


	while True:
		if(dir == "0"):
			servo_left()


		elif(dir == "1"):
			servo_right()


		else:
			break

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
