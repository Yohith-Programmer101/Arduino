import serial

con = serial.Serial('/dev/ttyACM0', 9600)
while True:
    print(con.readline().decode('utf-8'))
