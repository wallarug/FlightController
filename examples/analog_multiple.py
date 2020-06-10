import time
import board
import busio

from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

spdbrk = AnalogIn(board.SERVO5)
flaps = AnalogIn(board.SERVO6)

thr1 = AnalogIn(board.RCC1)
thr2 = AnalogIn(board.RCC2)
thr3 = AnalogIn(board.RCC3)
thr4 = AnalogIn(board.RCC4)

axes = [thr1, thr2, thr3, thr4, spdbrk, flaps]


def get_voltage(pin):
    return (pin.value * 3.3) / 65536

def get_percentage(pin):
    _max = 100
    _min = 0
    
    return (100 - ((pin.value * 3.3 / 65536) / 2.54 * 100))

report = ""

 
while True:
    report = ""

    for axis in axes:
        report += str(get_voltage(axis)) + ", "

    print(report)

    time.sleep(0.1)
