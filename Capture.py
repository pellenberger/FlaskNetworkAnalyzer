from subprocess import Popen
from shutil import copyfile
import time
from os import listdir, remove
from os.path import dirname
from Packet import Packet
from conf import INTERFACE

here = dirname(__file__)
CURRENT_CAPTURE_PATH = '{0}/captures/current'.format(here)
LIST_CAPTURES_PATH = '{0}/captures/list'.format(here)

class Capture:
	
	def __init__(self, name = ''):		
		self.proc = None
		self.name = name
		if name != '':
			self.load_packets()

	def start(self):
		self.proc = Popen(['tshark', 'port', '80', '-N', 'n', '-i', INTERFACE], stdout=open(CURRENT_CAPTURE_PATH, 'w'))
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
					time = splitted[0]
					src = splitted[1]
					dst = splitted[3]
					self.packets.append(Packet(src, dst, time))
				except :
					pass				

	def get_packets_count(self):
		return len(self.packets)

	def delete(self):
		remove('{0},{1}'.format(LIST_CAPTURES_PATH, self.name))

	@staticmethod
	def get_list_captures():
		captures = list()
		filenames = sorted(listdir(LIST_CAPTURES_PATH), reverse=True)
		for filename in filenames :
			captures.append(Capture(filename))
		return captures
