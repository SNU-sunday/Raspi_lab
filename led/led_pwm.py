"""
@author: Juhyeong Kang
"""

from __future__ import print_function, division
from RPi import GPIO
from time import sleep

__author__ = "Juhyeong Kang"
__email__ = "jhkang@astro.snu.ac.kr"

def setup(pin, hz):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)
    print('Setting the GPIO modes to BCM Numbering')
    print('The number of BCM pin is:  %i'%pin)
    return GPIO.PWM(pin, hz)

def pwminc(pwm, hz, delay):
    for i in range(hz+1):
        pwm.ChangeDutyCycle(i)
        sleep(delay)
    print('Increase the LED brightness')
        
def pwmdec(pwm, hz, delay):
    for i in range(hz, -1, -1):
        pwm.ChangeDutyCycle(i)
        sleep(delay)    
    print('Decrease the LED brightness')
    
def main(pin, pwm):
    delay = 0.01
    key = int(input('The LED light // 1: inc, 2: dec, 3: rep \n'))
    if key == 1:
        pwminc(pwm, hz, delay)
        main(pin, pwm)
    elif key == 2:
        pwmdec(pwm, hz, delay)
        main(pin, pwm)
    elif key == 3:
        print('-----------------------------')
        print('Repeat the brightness change')
        print('-----------------------------')
        while True:
            pwminc(pwm, hz, delay)
            pwmdec(pwm, hz, delay)
            
    else:
        ValueError('The mode shuld be the number from 1 to 3.')
    
if __name__ == '__main__':
    pin = int(input('Enter the correct BCM pin number:  '))
    hz = 100
    pwm = setup(pin, hz)
    pwm.start(0)
    try:
        main(pin, pwm)
    except KeyboardInterrupt:
        pwm.stop()
        print('Stop the PWM')
        GPIO.cleanup()
        print('Clean up the GPIO')