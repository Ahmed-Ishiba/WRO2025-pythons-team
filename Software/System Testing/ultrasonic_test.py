from gpiozero import DistanceSensor

ultrasonic1 = DistanceSensor(echo=20,trigger=6) #,pin_factory=factory
ultrasonic2 = DistanceSensor(echo=21,trigger=26)

while True:
	print("first ultrasonic",ultrasonic1.distance*100,"\n")
	print("second ultrasonic",ultrasonic2.distance*100)
