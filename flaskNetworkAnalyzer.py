#!/usr/bin/python
# coding: utf-8

from flask import Flask
from environment import DEBUG
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello from Flask!'

if __name__ == '__main__':
    app.run(debug=DEBUG) 
