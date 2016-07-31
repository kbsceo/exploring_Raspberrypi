import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# 16번 핀을 사용합시다.
PIN = 16
TRIG = 18
ECHO = 19

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)

def camera_run () :
    camera = picamera.PiCamera()
    camera.capture('./image01.jpg')

def distance_run () :
    while True :
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0 :
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1 :
            pulse_end = time.time()
        pulse_duration = pulse_duration * 17150
        distance = round(distance, 2)

GPIO.setup(PIN,GPIO.IN)

while True:
    if GPIO.input(PIN)==1:
        camera_run()
        distance_run()
        print("Detected!")  
    time.sleep(1)
