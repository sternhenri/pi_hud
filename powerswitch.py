import time
import RPi.GPIO as io
io.setmode(io.BCM)

yellowPin = 18
bluePin = 23
greenPin = 24
io.setup(yellowPin, io.OUT)
io.setup(bluePin, io.OUT)
io.setup(greenPin, io.OUT)

io.output(yellowPin, True)
io.output(bluePin, True)
io.output(greenPin, True)
while True:
	io.output(yellowPin, False)
	time.sleep(1)
	io.output(yellowPin, True)
	io.output(bluePin, False)
	time.sleep(1)
	io.output(bluePin, True)
	io.output(greenPin, False)
	time.sleep(1)
	io.output(greenPin, True)
