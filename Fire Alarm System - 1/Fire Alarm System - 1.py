import pyfirmata
from time import sleep

board = pyfirmata. Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

init_led = board.get_pin('d:11:o')
warn_led = board.get_pin('d:13:o')
buz = board.get_pin('d:12:o')
fire_sensor = board.get_pin('d:10:i')

init_led.write(1)


def reset():
    init_led.write(0)
    warn_led.write(0)
    buz.write(0)


def warn():
    print(f"{'='*10} !Fire! {'='*10}")
    warn_led.write(1)
    buz.write(1)


def normal():
    init_led.write(1)


while True:
    sleep(0.5)
    reset()
    value = fire_sensor.read()
    if value is None:
        pass
    elif value is True:
        normal()

    else:
        warn()

board.exit()
