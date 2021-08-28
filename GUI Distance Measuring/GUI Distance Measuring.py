import serial
import asyncio
import websockets

con = serial.Serial('/dev/ttyACM0', 9600)


async def measure(websocket, path):
    while True:
        distance = con.readline().decode('utf-8')
        await websocket.send(con.readline().decode('utf-8'))

start_webserver = websockets.serve(measure, "192.168.108.195", 5678)
asyncio.get_event_loop().run_until_complete(start_webserver)
asyncio.get_event_loop().run_forever()
