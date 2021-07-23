import pyfirmata
from time import sleep

board = pyfirmata.Arduino('/dev/ttyACM0')
board.digital[13].write(1)  # LED in pin 13
print("ON!")
for i in range(1, 11):
    sleep(1)
    print(i)
print("OFF!")
board.digital[13].write(0)
board.exit()
