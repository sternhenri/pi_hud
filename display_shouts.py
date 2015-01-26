#!flask/bin/python
from flask import Flask
from flask import request
import time
import RPi.GPIO as io

app = Flask(__name__)

def setup_hardware():
	io.setmode(io.BCM)

	global yellowPin
	yellowPin = 18
	global bluePin
	bluePin = 23
	global greenPin
	greenPin = 24
	io.setup(yellowPin, io.OUT)
	io.setup(bluePin, io.OUT)
	io.setup(greenPin, io.OUT)
	global on 
	on = False
	global off
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

@app.route('/display/<event>')
def display(event):

	print request.remote_addr
#	if request.remote_addr != '107.170.62.101':
#		return {'error': 'Access denied'}, 403
#	else:
#		return 'OK'

#need callback instead
	
	if event == 'post':
		color = 'yellow'
	elif event == 'signup':
		color = 'blue'
	elif event == 'sale':
		color = 'green'

	switch_light(color, on)
	time.sleep(3)
	switch_light(color, off)
	return 'OK'

if __name__ == '__main__':
	setup_hardware()
	turn_off_lights()
	app.run(host='0.0.0.0')

