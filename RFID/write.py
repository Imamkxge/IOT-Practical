import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Looking for cards")
print("Press Ctrl+C to stop")

try:
	text = input("Enter New Data: ")
	print("Place your tag to write...")
	reader.write(text)
	print("Data Written Successfully")
finally:
	GPIO.cleanup()
