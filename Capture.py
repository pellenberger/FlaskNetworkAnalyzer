from subprocess import Popen
from shutil import copyfile
import time
from os import listdir

CURRENT_CAPTURE_PATH = 'captures/current'
LIST_CAPTURES_PATH = 'captures/list'

class Capture:
	
	def __init__(self, name = ''):
		self.proc = None
		self.name = name

	def start(self):
		self.proc = Popen(['tshark', 'port', '80'], stdout=open(CURRENT_CAPTURE_PATH, 'w'))
		self.name = time.strftime('%d.%m.%Y %X')

	def stop(self):
		if self.proc == None:
			return
		self.proc.terminate()
		self.proc = None
		copyfile(CURRENT_CAPTURE_PATH, '{0}/{1}'.format(LIST_CAPTURES_PATH, self.name))		

	def is_running(self):
		if self.proc == None:
			return False
		else:
			return True

	@staticmethod
	def get_list_captures():
		captures = list()
		filenames = listdir(LIST_CAPTURES_PATH)
		for filename in filenames :
			captures.append(Capture(filename))
		return captures
