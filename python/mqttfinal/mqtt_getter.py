import paho.mqtt.client as mqtt

#from forwards import *
from cam_left import *
from cam_right import *
#from links_motorsteuerung import *
#from rechts_motorsteuerung import *
#from back_fahren_evtl_falsch import *
from aufraumen import *
from setup import *


url = "broker.mqttdashboard.com"
topic = "Radio-Cop"
id= "clientId-OSIU0td3NS"


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)


 
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    
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
client = paho.Client(client_id= id, clean_session=True, userdata=None, protocol=paho.MQTTv311)       #Client object
client.on_connect = on_connect #Callbacks registrieren
client.on_message = on_message

client.connect(url, 8000, 60)  #Connect
client.loop_forever()          #Abarbeiten von Paketen






