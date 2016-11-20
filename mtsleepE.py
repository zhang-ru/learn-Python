#recommend this way, instance object of threading.Thread
import threading
import time

loops = [4,2]

class MyThreading(threading.Thread):
	"""docstring for MyThreading"""
	def __init__(self, fun,args, name=''):
		threading.Thread.__init__(self)
		self.args = args
		self.fun = fun
		self.name = name
	def run(self): #re-write the run method
		self.fun(*self.args)
		

def loop(nloop,nsecd):
	print('loop',nloop,'start at: ',time.ctime())
	time.sleep(nsecd)
	print('loop',nloop,'end at: ',time.ctime())

def main():
	print("main start at:",time.ctime())
	nloops = range(len(loops))
	threads = []
	for i in nloops:
		thread = MyThreading(loop,(i,loops[i]),loop.__name__)
		threads.append(thread)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
	print("main end at:",time.ctime())

if __name__ == "__main__":
	main()
