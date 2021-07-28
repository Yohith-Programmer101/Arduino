import pyfirmata
from time import sleep

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

led = board.get_pin('d:13:o')
buz = board.get_pin('d:12:o')
pir = board.get_pin('d:2:i')


def detected():
    print("Motion Detected!")
    led.write(1)
    buz.write(1)


def not_detected():
    led.write(0)
    buz.write(0)


while True:
    value = pir.read()
    if value is None:
        pass
    elif value is False:
        not_detected()
    else:
        detected()
