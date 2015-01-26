#!flask/bin/python
from flask import Flask
import time
import RPi.GPIO as io

app = Flask(__name__)

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

def switch_light(color, switch_type):
	pin = -1
	if color == 'yellow':
		pin = yellowPin
	elif color == 'blue':
		pin = bluePin
	elif color == 'green':
		pin = greenPin

	io.output(pin, switch_type)

@app.route('/shout_display/<event>/<data>')
def parse_event(event, data):
    if event == 'post':
    	color = 'yellow'
    elif event == 'signup':
    	color = 'blue'
    elif event == 'sale':
    	color = 'green'

    switch_light(color, on)
    time.sleep(3)
    switch_light(color, off)


if __name__ == '__main__':
	setup_hardware()
	turn_off_lights()
	app.run()

