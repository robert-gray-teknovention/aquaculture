import RPi.GPIO as GPIO
import time
bottomSocket=5
topSocket=6

GPIO.setmode(GPIO.BCM)
GPIO.setup(bottomSocket, GPIO.OUT)
GPIO.setup(topSocket, GPIO.OUT)

while True:
    GPIO.output(bottomSocket, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(topSocket, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(bottomSocket, GPIO.LOW)
    time.sleep(5)
    GPIO.output(topSocket, GPIO.LOW)
    time.sleep(5)
    