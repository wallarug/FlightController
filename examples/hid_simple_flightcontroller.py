import board
import digitalio
import analogio
import usb_hid

# Run using Robo HAT MM1

from adafruit_hid.gamepad import Gamepad

gp = Gamepad(usb_hid.devices)

# Create some buttons. The physical buttons are connected
# to ground on one side and these and these pins on the other.
# Engine Ignition
button_pins = (board.SERVO1, board.SERVO2, board.SERVO3, board.SERVO4)

# Map the buttons to button numbers on the Gamepad.
# gamepad_buttons[i] will send that button number when buttons[i]
# is pushed.
gamepad_buttons = (1, 2, 8, 15)

buttons = [digitalio.DigitalInOut(pin) for pin in button_pins]
for button in buttons:
    button.direction = digitalio.Direction.INPUT
    button.pull = digitalio.Pull.UP

# Center console controls for 747 (6 levers)
thr1 = analogio.AnalogIn(board.RCC1)
thr2 = analogio.AnalogIn(board.RCC2)
thr3 = analogio.AnalogIn(board.RCC3)
thr4 = analogio.AnalogIn(board.RCC4)
flap = analogio.AnalogIn(board.SERVO5)
spdbrk = analogio.AnalogIn(board.SERVO6)

# reverse thrust (TODO: maybe buttons?)
#rthr1 = analogio.AnalogIn(board.RCC1)
#rthr2 = analogio.AnalogIn(board.RCC2)
#rthr3 = analogio.AnalogIn(board.RCC3)
#rthr4 = analogio.AnalogIn(board.RCC4)

# Equivalent of Arduino's map() function.
def range_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    # Buttons are grounded when pressed (.value = False).
    for i, button in enumerate(buttons):
        gamepad_button_num = gamepad_buttons[i]
        if button.value:
            gp.release_buttons(gamepad_button_num)
            print(" release", gamepad_button_num, end="")
        else:
            gp.press_buttons(gamepad_button_num)
            print(" press", gamepad_button_num, end="")

    # Convert range[0, 65535] to -127 to 127
    gp.move_joysticks(
        x=range_map(ax.value, 0, 65535, -127, 127),
        y=range_map(ay.value, 0, 65535, -127, 127),
    )
    print(" x", ax.value, "y", ay.value)
