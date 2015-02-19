import time
import picamera
import RPi.GPIO as GPIO # new

GPIO.setmode(GPIO.BCM) #new
GPIO.setup(14, GPIO.IN, GPIO.PUD_UP) # new
#def printFunction(channel):
#	print("Button 1 pressed")
#	print("Note how the bouncetime affects the button press")
#	GPIO.add_event_detect(14, GPIO.RISING, callback=printFunction, bouncetime=100)

with picamera.PiCamera() as camera:
	while True:
		print("Aqui 1")
		GPIO.wait_for_edge(14, GPIO.FALLING)
		print("Desligado")
	
		GPIO.wait_for_edge(14, GPIO.RISING)
		print("Aqui 2")
		camera.start_preview()
                print("Ligado")
                camera.capture_sequence([
                       	'image1.jpg',
                       	'image2.jpg',
                       	'image3.jpg',
                                       ])

camera.stop_preview()
GPIO.cleanup()
#			camera.start_preview()
#			print("aqui 1")
#			if GPIO.input(14) == GPIO.HIGH:
#				print("aqui 2")
#				camera.capture_sequence([
#					'image1.jpg',
#      					'image2.jpg',
#      					'image3.jpg',
#					]) 
#				camera.stop_preview()
#				print("Tirei Foto")
#			if GPIO.input(14) == GPIO.LOW:
#				print("Nao tem foto")
#			
#GPIO.cleanup()	
