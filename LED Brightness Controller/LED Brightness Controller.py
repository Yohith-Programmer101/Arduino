import pyfirmata
import time

board = pyfirmata. Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

try:
    print("Try turning the potentiometer!")
    time.sleep(1)
    print("Now try to Press Ctrl+C to stop the program and again turn the potentiometer, it should work even when the program is stopped!")
    while True:
        pass
except KeyboardInterrupt:
    board.exit()
    exit()
