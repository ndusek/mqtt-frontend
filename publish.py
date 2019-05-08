import paho.mqtt.client as paho
import sys
import random



broker="broker.hivemq.com"
#broker="broker.mqttdashboard.com"
port=1883
#port=8000
topic="bison457"

def on_publish(client,userdata,result):             #create function for callback
    print("published")
    pass

upper = 10
x = round(random.random()*upper, 7)
y = round(random.random()*upper, 7)
z = round(random.random()*upper, 7)
data = "{} {} {}".format(x,y,z)
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
print(data)
ret= client1.publish(topic,data)                   #publish
print(ret)
