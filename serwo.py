import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12, GPIO.OUT)

serwo = GPIO.PWM(12, 50) #Nowa instancja PWM
serwo.start(1/20*100) #Uruchomienie sygnału PWM

try:
	while True:
		i = 0.5
		while i <= 2.5:
			serwo.ChangeDutyCycle(i/20*100)
			print(i)
			i += 0.05
			time.sleep(0.1)
		while i >= 0.5:
			serwo.ChangeDutyCycle(i/20*100)
			print(i)
			i -= 0.05
			time.sleep(0.1)
except KeyboardInterrupt:
	print('Koniec')

serwo.stop()
GPIO.cleanup()