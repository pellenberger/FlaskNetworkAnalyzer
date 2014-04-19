#!/usr/bin/python
# coding: utf-8

from flask import Flask, render_template
from environment import DEBUG
from Capture import Capture
app = Flask(__name__)

current_capture = Capture()

@app.route('/')
def index():	
	if current_capture.is_running() == True:
		return render_template('stop_capture.html')
	else:
	    return render_template('start_capture.html')	

@app.route('/capture/start', methods=['GET', 'POST'])
def start_capture():
	if current_capture.is_running() == True:
		return index()
	current_capture.start()
	return render_template('stop_capture.html')	

@app.route('/capture/stop', methods=['GET', 'POST'])
def stop_capture():
	if current_capture.is_running() == False:
		return index()
	current_capture.stop()
	return render_template('start_capture.html')

if __name__ == '__main__':
    app.run(debug=DEBUG) 
