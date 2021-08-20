import time
import pyfirmata
import json

board = pyfirmata.Arduino('/dev/ttyACM0')
board.digital[13].write(0)
data = {}

while True:
    time.sleep(0.5)
    try:
        with open("First GUI Project/state.json", "r") as f:
            data = json.loads(f.read())
    except:
        pass
    board.digital[13].write(data["state"])

board.exit()
