import pyfirmata
import time

board = pyfirmata. Arduino('/dev/ttyACM0')
pin = 13
board.digital[pin].mode = pyfirmata.SERVO


def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)


while True:
    for i in range(0, 180):
        setServoAngle(pin, i)
    for i in range(180, 1, -1):
        setServoAngle(pin, i)

board.exit()
