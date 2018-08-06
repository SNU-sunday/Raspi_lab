"""
@author: Juhyeong Kang
"""

from __future__ import print_function, division
from RPi import GPIO
from time import sleep

__author__ = "Juhyeong Kang"
__email__ = "jhkang@astro.snu.ac.kr"

def MAP(x, im, iM, om, oM):
    return (x - im) * (oM - om) / (iM - im)

class rgbLED(object):
    def __init__(self):
        self.colors = {'r': 0xFF0000, 'g': 0x00FF00, 'b': 0x0000FF,
                       'y': 0xFFFF00, 'p': 0xFF00FF, 'c': 0X00FFFF,
                       'w': 0xFFFFFF}
        self.pins = {}
        self.pins['r'] = int(input('insert the pin number of red lamp:  '))
        self.pins['g'] = int(input('insert the pin number of green lamp:  '))
        self.pins['b'] = int(input('insert the pin number of blue lamp:  '))
        self.pwms = {}
    def setup(self):
        GPIO.setmode(GPIO.BCM)
        for i in self.pins.values():
            GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW)
        self.pwms['r'] = GPIO.PWM(self.pins['r'],2000)
        self.pwms['g'] = GPIO.PWM(self.pins['g'],2000)
        self.pwms['b'] = GPIO.PWM(self.pins['b'],2000)
        
        for i in self.pwms.values():
            i.start(0)
    

    def setColor(self, color):
        Rv = (color & 0xFF0000) >> 16
        Gv = (color & 0x00FF00) >> 8
        Bv = (color & 0x0000FF) >> 0
        
        Rv = MAP(Rv, 0, 255, 0, 100)
        Gv = MAP(Gv, 0, 255, 0, 100)
        Bv = MAP(Bv, 0, 255, 0, 100)
        
        self.pwms['r'].ChangeDutyCycle(Rv)
        self.pwms['g'].ChangeDutyCycle(Gv)
        self.pwms['b'].ChangeDutyCycle(Bv)
        
        
    def rainbow(self):
        for i in range(101):
            self.pwms['r'].ChangeDutyCycle(100-i)
            self.pwms['g'].ChangeDutyCycle(i)
            sleep(0.05)
        for i in range(101):
            self.pwms['g'].ChangeDutyCycle(100-i)
            self.pwms['b'].ChangeDutyCycle(i)
            sleep(0.05)
        for i in range(101):
            self.pwms['r'].ChangeDutyCycle(i)
            sleep(0.05)
    
    def destroy(self):
        for i in self.pwms.values():
            i.stop()
        for i in self.pins.values():
            GPIO.output(i, GPIO.LOW)
        GPIO.cleanup()
