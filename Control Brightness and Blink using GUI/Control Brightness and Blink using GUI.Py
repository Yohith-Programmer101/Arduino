import pyfirmata
import time
import json

board = pyfirmata.Arduino('/dev/ttyACM0')
led = board.get_pin('d:11:p')
data = {}

while True:
    time.sleep(0.5)
    try:
        with open("Control Brightness and Blink using GUI/data.json", "r") as f:
            data = json.loads(f.read())
    except:
        pass
    led.write(data["brightness"])
    time.sleep(data["delay"])
    led.write(0)

board.exit()
