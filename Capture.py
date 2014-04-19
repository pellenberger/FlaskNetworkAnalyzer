from subprocess import Popen
from shutil import copyfile
import time

class Capture:
	
	def __init__(self):
		self.proc = None

	def start(self):
		self.proc = Popen(['tshark'], stdout=open('captures/current', 'w'))
		self.name = time.strftime('%d.%m.%Y %X')

	def stop(self):
		if self.proc == None:
			return
		self.proc.terminate()
		self.proc = None
		copyfile('captures/current', 'captures/list/{0}'.format(self.name))		

	def is_running(self):
		if self.proc == None:
			return False
		else:
			return True
