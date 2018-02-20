# -*- coding: utf-8 -*-
from entryboard import *
import RPi.GPIO as GPIO

switches = [SW1, SW2, SW3, SW4]
leds = [LED1, LED2, LED3, LED4]
led5 = [LED5_R, LED5_G, LED5_B]
led6 = [LED6_R, LED6_G, LED6_B]
GPIO.setmode(GPIO.BCM)

# スイッチとLEDの初期化
GPIO.setup(switches, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led5, GPIO.OUT initial=GPIO.LOW)
GPIO.setup(led6, GPIO.OUT initial=GPIO.LOW)
