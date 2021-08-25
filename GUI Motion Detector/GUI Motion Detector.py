import pyfirmata
from time import sleep
import asyncio
import websockets

board = pyfirmata.Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()

led = board.get_pin('d:13:o')
buz = board.get_pin('d:12:o')
pir = board.get_pin('d:2:i')

current_state = 0
before_state = 0


async def detect_pir(websocket, path):
    global before_state, current_state
    while True:
        value = pir.read()
        if value is None:
            pass
        elif value is True:
            current_state = 1
            led.write(1)
            buz.write(1)
            if current_state == before_state:
                pass
            else:
                await websocket.send('1')
        else:
            current_state = 0
            led.write(0)
            buz.write(0)
            if current_state == before_state:
                pass
            else:
                await websocket.send('0')
        before_state = current_state


start_server = websockets.serve(detect_pir, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
