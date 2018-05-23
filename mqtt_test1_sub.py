import paho.mqtt.client as mqtt

url = "broker.mqttdashboard.com"
topic = "haw/dmi/mt/its/ss18"
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    if payload == '0':
        print("Schalte Licht aus")
    elif payload == '1':
        print("Schalte Licht ein")
    else:
        print("unbekannter Befehl")

#Hier gehts los
client = mqtt.Client()         #Client object
client.on_connect = on_connect #Callbacks registrieren
client.on_message = on_message

client.connect(url, 1883, 60)  #Connect
client.loop_forever()          #Abarbeiten von Paketen
