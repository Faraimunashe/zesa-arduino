import serial

serial_port = 'COM7'
arduino = serial.Serial(serial_port, 9600, timeout=2)
data = "0"
    
arduino.write(data.encode())

arduino.close()