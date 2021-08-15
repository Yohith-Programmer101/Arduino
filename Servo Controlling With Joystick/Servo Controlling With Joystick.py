import pyfirmata
import time

board = pyfirmata. Arduino('/dev/ttyACM0')
it = pyfirmata.util.Iterator(board)
it.start()
pinX = 13
pinY = 12
board.digital[pinX].mode = pyfirmata.SERVO
board.digital[pinY].mode = pyfirmata.SERVO
joyX = board.get_pin('a:0:i')
joyY = board.get_pin('a:1:i')


def setServoAngle(pin, angle):
    board.digital[pin].write(angle)


while True:
    time.sleep(0.15)
    if joyX.read() != None:
        val = int(round(joyX.read(), 1)*180)
        setServoAngle(pinX, val)
    if joyY.read() != None:
        val = int(round(joyY.read(), 1)*180)
        setServoAngle(pinY, val)

board.exit()
