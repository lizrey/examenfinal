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
    usuario="licha_05reyes@outlook.com"
    password="Galapagos1001"
    Stopic="licha_05reyes@outlook.com/IoT1"
    SendTopic="licha_05reyes@outlook.com/IoT"
    GPIO.setup(pulsador,GPIO.IN)
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(pulsador1,GPIO.IN)
    GPIO.setup(led1,GPIO.OUT)

    mqttc=mqtt.Client()
    mqttc.username_pw_set(usuario,password)
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe(Stopic,0)
    info="0"
    while(1):
        mqttc.loop()
        f=open("informacion.txt","a")
        info=str(datetime.now())
        if(GPIO.input(pulsador)==0):
            f.write("- "+info+" se ha presionado el pulsador uno\n")
            f=open("informacion.txt","r")
            GPIO.output(led,1)
            mqttc.publish(SendTopic,"on/off")
            time.sleep(1)
            mqttc.publish(SendTopic,"off/off/"+f.read())
            f.close()
        
        if(GPIO.input(pulsador1)==0):
            
            f.write("- "+info+" se ha presionado el pulsador dos\n")
            f=open("informacion.txt","r")
            GPIO.output(led1,1)
            mqttc.publish(SendTopic,"off/on")
            time.sleep(1)
            mqttc.publish(SendTopic,"off/off/"+f.read())
            f.close()
        
        
        
        GPIO.output(led,0)
        GPIO.output(led1,0)
        
        
        
            
