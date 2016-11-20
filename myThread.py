# build myThread objec
import threading
import time

class MyThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, func, args, name = ''):
		threading.Thread.__init__(self)
		self.args = args
		self.func = func
		self.name = name

	def getResult(self):
		return self.res

	def run(self):
		print('startting', self.name, 'at:', time.ctime())
		self.res = self.func(*self.args)
		print(self.name,'finished at:',time.ctime())

