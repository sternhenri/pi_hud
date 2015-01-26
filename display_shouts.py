#!flask/bin/python
from flask import Flask
import time
import RPi.GPIO as io

def setup_hardware():
	io.setmode(io.BCM)

	yellowPin = 18
	bluePin = 23
	greenPin = 24
	io.setup(yellowPin, io.OUT)
	io.setup(bluePin, io.OUT)
	io.setup(greenPin, io.OUT)
	on = False
	off = True

def turn_off_lights():
	io.output(yellowPin, off)
	io.output(bluePin, off)
	io.output(greenPin, off)
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
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)

