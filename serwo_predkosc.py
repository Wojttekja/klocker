import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

serwoL = GPIO.PWM(12, 50) #Nowa instancja PWM
serwoL.start(1/20*100) #Uruchomienie sygnału PWM
serwoR = GPIO.PWM(13, 50)
serwoR.start(1/20*100)
serwo = GPIO

try:
	while True:
		predkosc = float(input())
		serwoL.ChangeDutyCycle(predkosc/20*100)
		serwoR.ChangeDutyCycle(predkosc/20*100)
except KeyboardInterrupt:
	print('Koniec')

serwo.stop()
GPIO.cleanup()