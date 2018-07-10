import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)
c= 0  #counter
p.start(7.5)  #startposition  c=0
time.sleep(.2)
#GPIO.cleanup()
global c

def cright():
	
	if c == -4:
		p.start(10.5)
		c=c+1
	elif c == -3:
		p.start(9.5)
		c=c+1
	elif c == -2:
		p.start(8.5)
		c=c+1
	elif c == -1:
		p.start(7.5)
		c=c+1
	elif c==0:
		p.start(6.5)
		c=c+1  
	elif c == 1:
		p.start(5.5)
		c=c+1
	elif c == 2:
		p.start(4.5)
		c=c+1
	elif c == 3:
		p.start(3.5)
		c=c+1
	else: 
		print("FATAL ERROR CAM")
	
	print (c)
	time.sleep(.2)
	#p.stop()
	#GPIO.cleanup()

def cleft():
	
	if c == -3:
		p.start(11.5)
		c=c-1
	elif c == -2:
		p.start(10.5)
		c=c-1
	elif c == -1:
		p.start(9.5)
		c=c-1
	elif c==0:
		p.start(8.5)
		c=c-1  
	elif c == 1:
		p.start(7.5)
		c=c-1
	elif c == 2:
		p.start(6.5)
		c=c-1
	elif c == 3:
		p.start(5.5)
		c=c-1
	elif c == 4:
		p.start(4.5)
		c=c-1
		
	else: 
		print("FATAL ERROR CAM")
	
	print (c)
	time.sleep(.2)
	#p.stop()
	#GPIO.cleanup()