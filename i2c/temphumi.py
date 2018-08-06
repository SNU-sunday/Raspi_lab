"""
@author: Juhyeong Kang
"""

from __future__ import print_function, division
import smbus
from time import sleep


__author__ = "Juhyeong Kang"
__email__ = "jhkang@astro.snu.ac.kr"

th_address = 0x40
T_L = 0x00
T_H = 0x01
H_L = 0X02
H_H = 0X03
Interrupt_drdy = 0x04
T_max = 0x05
H_max = 0x06
Interrupt_conf = 0x07
T_offset_adjust = 0x08
H_offset_adjust = 0x09
T_thr_L = 0x0A
T_thr_H = 0x0B
H_thr_L = 0x0C
H_thr_L = 0x0D
conf = 0x0E
measurement_conf = 0x0F
mid_L = 0xFC
mid_H = 0xFC
Device_id_l = 0xFE
Device_id_l = 0xFF



humi_address = 0x


i2c_bus = smbus.SMBus(1)
TEMP = ic2_bus.read_byte_data(th_address, temp_address)
HUMI = ic2_bus.read_byte_data(th_address, humi_address)