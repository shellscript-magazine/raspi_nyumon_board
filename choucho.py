# -*- coding: utf-8 -*-
import time
import pigpio

BUZZER = 18
gpio = pigpio.pi()
gpio.set_mode(BUZZER, pigpio.OUTPUT)

##1オクターブの周波数
scale = [ 523.251, 587.33, 659.255, 698.456, 783.991, 880, 987.767, 1046.502 ]
##ド=0、レ=1、ミ=2、ファ=3、ソ=4、ラ=5、シ=6、ド=7、4分音符（+0）、2分音符（+10）
##曲（ちょうちょ）
music = [4,2,12,3,1,11,0,1,2,3,4,4,14,4,2,2,2,3,1,1,1,0,2,4,4,2,2,12]

try:
	for note in music:
            if note >= 10:
                note = note - 10
                gpio.hardware_PWM(BUZZER, scale[note], 500000)
                time.sleep(1)
            else:
                gpio.hardware_PWM(BUZZER, scale[note], 500000)
                time.sleep(0.5)
            gpio.hardware_PWM(BUZZER,0 ,0)
	    time.sleep(0.1)
except KeyboardInterrupt:
	gpio.hardware_PWM(BUZZER, 0, 0)
        gpio.stop()
