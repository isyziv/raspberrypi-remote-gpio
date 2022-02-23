from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep
import json
with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)
#################################################
factory = PiGPIOFactory(host=jdata['ip'])
#################################################
led = LED(17, pin_factory=factory)

while True:
    led.on()
    sleep(0.05)
    led.off()
    sleep(0.05)