#!/usr/bin/python
# coding: utf-8

from flask import Flask, render_template, redirect, url_for
from environment import DEBUG
from Capture import Capture
app = Flask(__name__)

current_capture = Capture()

@app.route('/')
def index():
	if current_capture.is_running() == True:
		return render_template('stop_capture.html', captures = Capture.get_list_captures())
	else:
	    return render_template('start_capture.html', captures = Capture.get_list_captures())	

@app.route('/capture/start', methods=['GET', 'POST'])
def start_capture():
	if current_capture.is_running() == True:
		return index()
	current_capture.start()
	return render_template('stop_capture.html', captures = Capture.get_list_captures())	

@app.route('/capture/stop', methods=['GET', 'POST'])
def stop_capture():
	if current_capture.is_running() == False:
		return index()
	current_capture.stop()
	return render_template('start_capture.html', captures = Capture.get_list_captures())

@app.route('/<capture_name>', methods=['GET'])
def show_capture(capture_name):
	return render_template('show_capture.html', capture = Capture(capture_name))

@app.route('/<capture_name>/delete', methods=['GET'])
def delete_capture(capture_name):
	Capture(capture_name).delete()
	return index()
	

if __name__ == '__main__':
    app.run(debug=DEBUG) 
