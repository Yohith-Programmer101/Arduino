import pyfirmata
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
led = board.get_pin('d:13:o')  # LED in pin 13
while True:
    led.write(1)
    time.sleep(1)
    led.write(0)
    time.sleep(1)
board.exit()
