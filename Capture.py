from subprocess import Popen
from shutil import copyfile
import time
from os import listdir
from Packet import Packet

CURRENT_CAPTURE_PATH = 'captures/current'
LIST_CAPTURES_PATH = 'captures/list'

class Capture:
	
	def __init__(self, name = ''):
		self.proc = None
		self.name = name
		if name != '':
			self.load_packets()

	def start(self):
		self.proc = Popen(['tshark', 'port', '80', '-N', 'n'], stdout=open(CURRENT_CAPTURE_PATH, 'w'))
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

	def load_packets(self):
		filename = '{0}/{1}'.format(LIST_CAPTURES_PATH, self.name)
		self.packets = list()
		with open(filename, 'r') as file:
			for line in file.readlines():
				splitted = line.strip().split(' ')
				try :
					src = splitted[1]
					dst = splitted[3]
					self.packets.append(Packet(src, dst))
				except :
					pass				

	def get_packets_count(self):
		return len(self.packets)

	@staticmethod
	def get_list_captures():
		captures = list()
		filenames = listdir(LIST_CAPTURES_PATH)
		for filename in filenames :
			captures.append(Capture(filename))
		return captures
