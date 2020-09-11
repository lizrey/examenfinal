from datetime import datetime
import time
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

pulsador=5
led=12
pulsador1=6
led1=13

def main():
    GPIO.setup(pulsador,GPIO.IN)
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(pulsador1,GPIO.IN)
    GPIO.setup(led1,GPIO.OUT)

    mqttc=mqtt.Client()
    mqttc.on_message=on_message
    mqttc.username_pw_set("jomsk@hotmail.com","Jomsk4all1996")
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe("jomsk@hotmail.com/IoT1",0)
    info=""
    while(1):
        mqttc.loop()
        f=open("informacion.txt","a")
        info=str(datetime.now())
        if(GPIO.input(pulsador)==0):
            f.write("- "+info+" se ha presionado el pulsador uno \n")
            f.close()
            GPIO.output(led,1)
            time.sleep(2)
            mqttc.publish("jomsk@hotmail.com/IoT","on/off")
            
        if(GPIO.input(pulsador1)==0):
            
            f.write("- "+info+" se ha presionado el pulsador dos \n")
            f.close()
            GPIO.output(led1,1)
            time.sleep(2)
            mqttc.publish("jomsk@hotmail.com/IoT","off/on")
            
        f = open("informacion.txt", "r")
        f.read()
        
        GPIO.output(led,0)
        GPIO.output(led1,0)
        mqttc.publish("jomsk@hotmail.com/IoT","off/off/"+f.read())
        
            
def on_message(client,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+msg.payload.decode('utf-8'))
            