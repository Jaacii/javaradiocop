import paho.mqtt.client as mqtt
url = "broker.mqttdashboard.com"
topic = "haw/dmi/mt/its/ss18/radiocop"
port = 1883
# 1883   default port
#from forwards import *
#from cam_left import *
#from cam_right import *
#from links_motorsteuerung import *
#from rechts_motorsteuerung import *
#from backwards import *
from aufraeumen import *
from setup import *



def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe(topic)


def on_message(client, userdata, msg):
        payload = msg.payload.decode('utf-8')
        if payload == '0':
                print("Stop")
                bremsen()
        elif payload == '1':
                print("Start")
                losfahren()
                pr.start(40)
                pl.start(40)
        elif payload == '10':
                print("links")
                links()
        elif payload == '01':
                print("rechts")
                rechts()
        elif payload == '101':
                print("Cam right")
                #cam_right()
        elif payload == '110':
                print("Cam left")
                #cam_left()
        elif payload == '111':
                print("Radio")
                #radiotoggle()

        else:
                print("unbekannter Befehl")


#Hier gehts los    paho.client? mqtt.client
client = mqtt.Client("", True, None, mqtt.MQTTv31) #Client object
client.on_connect = on_connect #Callbacks registrieren
client.on_message = on_message

client.connect(url, port, 60) #Connect
client.loop_forever() #Abarbeiten von Paketen