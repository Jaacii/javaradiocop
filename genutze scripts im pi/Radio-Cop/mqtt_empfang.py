import paho.mqtt.client as mqtt
import time
import os
url = "broker.mqttdashboard.com"
topic = "haw/dmi/mt/its/ss18/radiocop"
port = 1883
from radio import *
from fahrscript import *
from setup import *
from servo import *



def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(topic)
		pr.start(40)
		pl.start(40)


def on_message(client, userdata, msg):
        payload = msg.payload.decode('utf-8')
        if payload == 'stop':
                print("Stop")
                bremsen()
        elif payload == 'forward':
                print("Start")
                losfahren()
		elif payload == 'back':
                print("back")
                back()
        elif payload == 'links':
                print("links")
                links()
        elif payload == 'rechts':
                print("rechts")
                rechts()
        elif payload == 'CamR':
                print("Cam right")
                cright()
        elif payload == 'CamL':
                print("Cam left")
               cleft()
        elif payload == 'RadioAus':
                print("Radio")
				
				radio_aus()
			
		elif payload == '903':
				print("903")
                neunzigkommadrei()
		elif payload == 'sthh':
				print("Radio Hamburg")
                RadioHH()
		elif payload == 'ndr':
				print("NDR2")
                ndr()
        elif payload == 'reload':
				print("reload")
                
		
		else:
                print("unbekannter Befehl")


#Hier gehts los    paho.client? mqtt.client
client = mqtt.Client("", True, None, mqtt.MQTTv31) #Client object
client.on_connect = on_connect #Callbacks registrieren
client.on_message = on_message

client.connect(url, port, 60) #Connect
client.loop_forever() #Abarbeiten von Paketen