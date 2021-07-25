import pyfirmata
from time import sleep

board = pyfirmata.Arduino('/dev/ttyACM0')
leds1 = [6, 7, 8, 9, 10, 11, 12, 13]
leds2 = [13, 12, 11, 10, 9, 8, 7, 6]
while True:
    for i in leds1:
        board.digital[i].write(1)
        sleep(0.3)
    for i in leds2:
        board.digital[i].write(0)
        sleep(0.3)
board.exit()
