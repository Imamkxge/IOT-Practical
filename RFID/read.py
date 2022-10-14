import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Looking for cards...")
print("Press CTRL+C to stop")

try:
	id, text = reader.read()
	print(id)
	print(text)
finally:
	GPIO.cleanup()