import time
import board
import busio

from digitalio import DigitalInOut, Direction
from analogio import AnalogIn

analog_in = AnalogIn(board.RCC1)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536
 
 
while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
