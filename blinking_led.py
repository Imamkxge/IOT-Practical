import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

for i in range(10):
	GPIO.output(7, True)
	print("LED IS ON")
	time.sleep(2)

	GPIO.output(7, False)
	print("LED IS OFF")
	time.sleep(2)

print("Practical Accomplished")
GPIO.cleanup()