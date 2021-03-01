import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
led=14
sensor=4

GPIO.setup(led,GPIO.OUT)
GPIO.setup(sensor,GPIO.IN)

while 1 :
    if GPIO.input(sensor):
        GPIO.output(led,GPIO.HIGH)
    else :
        GPIO.output(led,GPIO.LOW)