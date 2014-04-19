from subprocess import Popen

class Capture:
	
	def __init__(self):
		self.proc = None

	def start(self):
		self.proc = Popen(['tshark'], stdout=open('captures/current', 'w'))

	def stop(self):
		if self.proc != None:
			self.proc.terminate()
			self.proc = None

	def is_running(self):
		if self.proc == None:
			return False
		else:
			return True
