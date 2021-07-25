import pyfirmata
from time import sleep

board = pyfirmata. Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

init_led = board.get_pin('d:11:o')
warn_led = board.get_pin('d:13:o')
buz = board.get_pin('d:12:o')
fire_sensor = board.get_pin('a:0:i')

init_led.write(1)


def reset():
    init_led.write(0)
    warn_led.write(0)
    buz.write(0)


def warn(val):
    print(f"{'='*10} Fire! {val*10}% near{'='*10}")
    warn_led.write(1)
    buz.write(1)


def normal():
    init_led.write(1)


while True:
    sleep(0.5)
    reset()
    # So many filters to the value because the flame sensor give values in decimal and in decreasing order.
    value = int(abs(round(fire_sensor.read(), 1)*10-10))
    if value is None:
        pass
    elif value <= 0:
        normal()
    elif value > 0:
        warn(value)
    else:
        pass

board.exit()
