import pyfirmata
import json
import time

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
pot = board.get_pin('a:0:i')
data = {}

while True:
    time.sleep(0.5)
    try:
        with open("Continuous Input From Potentiometer/data.json", "w") as f:
            f.write(json.dumps(pot.read()))
    except:
        pass

board.exit()
