import paho.mqtt.client as mqtt #import the client1
import time
import json
import math

def whenCalled(client, userdata, message):
    print("received " ,str(message.payload.decode("utf-8")))
    print("from topic ",message.topic)

broker = '10.245.156.154'
topic_sub = 'angles'
topic_pub = 'angles'

client = mqtt.Client("fred") # use a unique name
client.on_message = whenCalled # callback
client.connect(broker)
print('Connected to %s MQTT broker' % broker)

print("Opening points file")

filein = open("listangle.json")
anglelist = json.load(filein)
filein.close()

nPoints = len(anglelist[1])
    
def main():
    print("Starting position")
    
    shoulder = anglelist[0][0]
    elbow = anglelist[1][0]
    print("Shoulder angle: " + str(shoulder))
    print("Elbow angle: " + str(elbow))
    client.publish(topic_pub, "(" + str(shoulder) + "," + str(elbow) + ")")
    time.sleep(2)
    
    print("Sending angles")
    for i in range(1, nPoints):
        shoulder = anglelist[0][i]
        elbow = anglelist[1][i]
        print("Shoulder angle: " + str(shoulder))
        print("Elbow angle: " + str(elbow))
        client.publish(topic_pub, "(" + str(shoulder) + "," + str(elbow) + ")")
        time.sleep(0.25)
    
main()
