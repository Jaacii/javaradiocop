import os
import time

#def radio_an():
#	os.system("sudo /home/pi/Radio2/Radio2/Radio")		//nicht benutzt
	
def radio_aus():
#	os.system("gcc -o Radio_off /home/pi/Radio2/example/Radio_off.cpp /home/pi/Radio2/Si4703_Breakout.cpp -wiringPi")
#	rime.sleep(2)
	os.system("sudo /home/pi/Radio2/Radio_off")
	
def ndr():
	os.system("sudo /home/pi/Radio2/Radio2/NDR")
	
def neunzigkommadrei():
	os.system("sudo /home/pi/Radio2/Radio2/903")
	
def RadioHH():
	os.system("sudo /home/pi/Radio2/Radio2/StHH")