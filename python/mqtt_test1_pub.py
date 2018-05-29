import paho.mqtt.client as mqtt
import time

url = "broker.mqttdashboard.com"
topic = "haw/dmi/mt/its/ss18"

connected = False
def on_connect(client, userdata, flags, rc):
    global connected
    connected = True

#Hier gehts los
client = mqtt.Client()
client.on_connect = on_connect

client.connect(url, 1883, 60) #Connect


#Nächste Anweisung startet einen Thread
#Dies ermöglicht "blockende" Operationen
#Wie die Abfrage der Tastatur unten
client.loop_start()

#"Schöne" wait for connect Anzeige
print("Waiting for connection ", end='')
while not connected:
    print(".", end='')
    time.sleep(0.1)
print("[CONNECTED]")

#Warten auf Benutzereingabe
while 1:
    cmd = input('Licht an oder aus?')
    if cmd == 'an':
        cmd = '1'
    elif cmd == 'aus':
        cmd = '0'
    else:
        print("Programmabbruch. [an/aus] ist erlaubt")
        break

    #Hier wird die Nachricht gesendet
    client.publish(topic, cmd)

#Stoppen des Event-Threads
client.loop_stop()
