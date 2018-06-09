import paho.mqtt.client as mqtt
url = "broker.mqttdashboard.com"
topic = "haw/dmi/mt/its/ss18"
from forwards import *
from cam_left import *
from cam_right import *
from links_motorsteuerung import *
from rechts_motorsteuerung import *
from back_fahren_evtl_falsch import *



def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

	
	
def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    if payload == '0':
        print("Stop")
		bremsen1()
    elif payload == '1':
        print("Start")
		forwards()
	elif payload == '10':
       print("links")
		links_motorsteuerung()
	elif payload == '01':
        print("rechts")
		rechts_motorsteuerung()
	elif payload == '101':
        print("Cam right")
		cam_right()
	elif payload == '110':
        print("Cam left")
		cam_left()
	elif payload == '111':
        print("Radio")
		radiotoggle()	
		
    else:
        print("unbekannter Befehl")

		
		
#Hier gehts los
client = mqtt.Client()         #Client object
client.on_connect = on_connect #Callbacks registrieren
client.on_message = on_message

client.connect(url, 1883, 60)  #Connect
client.loop_forever()          #Abarbeiten von Paketen
