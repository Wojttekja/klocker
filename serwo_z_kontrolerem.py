from pygame import joystick, init, event
from time import sleep
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
serwoL = GPIO.PWM(12, 50) #Nowa instancja PWM
serwoL.start(1.4/20*100) #Uruchomienie sygnału PWM
GPIO.setup(13, GPIO.OUT)
serwoR = GPIO.PWM(13, 50)
serwoR.start(1.4/20*100)

serwoL.ChangeDutyCycle(1.4/20*100)
serwoR.ChangeDutyCycle(1.4/20*100)

init()
while True:
    if joystick.get_count() > 0:
        break   
    print("No controller detected")
    sleep(0.5)
print(f"Found {joystick.get_count()} joystick")
js = joystick.Joystick(0)
name = js.get_name()
js.init()
print(f"connected to {name}")

loop = True
while loop:
    event.clear()
    print(f"Lewe: {(round(js.get_axis(1), 2)+1.5)/20*100} \t Prawe: {(round(js.get_axis(3), 2)+1.5)/20*100}")
    # print(f"Lewe: {js.get_axis(1)} \t Prawe: {js.get_axis(3)}")
    serwoL.ChangeDutyCycle((round(js.get_axis(1), 2)+1.5)/20*100)
    serwoR.ChangeDutyCycle((round(js.get_axis(3), 2)+1.5)/20*100)
    sleep(0.2)
