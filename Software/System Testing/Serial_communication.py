import serial 
import time
ser = serial.Serial('/dev/ttyAMA2',9600, timeout=1)
ser.reset_input_buffer()

ser2 = serial.Serial('/dev/ttyAMA0',9600, timeout=1)
ser2.reset_input_buffer()

while True:
	try:
		yaw = int(ser.readline().decode('utf-8').strip())
		yaw_initial = int(yaw)
		while abs(int(yaw)-yaw_initial) !=90 :
			yaw = int(ser.readline().decode('utf-8').strip())
			print("turning")
			print(yaw)
		
		print("turned 90 deg")
		yaw_initial = yaw
	except ValueError:
		print("no yaw recieved")
	"""
	ser2.write(b"S\n")
"""
