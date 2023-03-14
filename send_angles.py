import time
import json
import math
from secrets import Tufts_Wireless as wifi
import mqtt_CBR

print("Opening points file")

filein = open("listangle.json")
anglelist = json.load(filein)
filein.close()

nPoints = len(anglelist[1])

mqtt_broker = '10.247.45.39' 
topic_pub = 'angles'
topic_sub = 'angles'
client_id = 'MyESP'

mqtt_CBR.connect_wifi(wifi)

print("Connected")
    
def whenCalled(topic, msg):
    print((topic.decode(), msg.decode()))
    time.sleep(0.5)
        
def main():
    fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
    
    print("Starting position")
    
    shoulder = anglelist[0][0]
    elbow = anglelist[1][0]
    print("Shoulder angle: " + str(shoulder))
    print("Elbow angle: " + str(elbow))
    fred.publish(topic_pub, "(" + str(shoulder) + "," + str(elbow) + ")")
    time.sleep(2)
    
    
    print("Sending angles")
    for i in range(1, nPoints):
        shoulder = anglelist[0][i]
        elbow = anglelist[1][i]
        print("Shoulder angle: " + str(shoulder))
        print("Elbow angle: " + str(elbow))
        fred.publish(topic_pub, "(" + str(shoulder) + "," + str(elbow) + ")")
        time.sleep(0.25)
    
main()
