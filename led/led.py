
from __future__ import print_function, division
from RPi import GPIO
import time

LEDpin = 20

def setup(LEDpin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDpin, GPIO.OUT, initial=GPIO.HIGH)
    print('Setting the GPIO modes to BCM Numbering')
    print('The number of BCM pin is:  %i'%LEDpin)
    
def on(LEDpin):
    GPIO.output(LEDpin, GPIO.LOW)
    print('LED ON')
    
def off(LEDpin):
    GPIO.output(LEDpin, GPIO.HIGH)
    print('LED OFF')
    
def blink(btime=0.5, LEDpin= 20):
    print('Blink mode ON')
    print('The interval of blink is %i'%btime)
    while True:
        on(LEDpin)
        time.sleep(btime)
        off(LEDpin)
        time.sleep(btime)

def destroy(LEDpin):
    off(LEDpin)
    print('System off.')
    GPIO.cleanup()

def main(LEDpin):
    key = int(input('Choose the LED mode // 1: on, 2: off, 3: blink : \n'))
    if key == 1:
        on(LEDpin)
        main(LEDpin)
    elif key == 2:
        off(LEDpin)
        main(LEDpin)
    elif key == 3:
        btime = float(input('please enter the blink interval in second : \n'))
        blink(btime, LEDpin)
    elif key > 4:
        ValueError('LED mode should be the number 1 to 3.')

if __name__ == '__main__':
    LEDpin = int(input('Enter the correct BCM pin number:  '))
    setup(LEDpin)
    try:
        main(LEDpin)
    except KeyboardInterrupt:
        destroy(LEDpin)