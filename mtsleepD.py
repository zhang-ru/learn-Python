#create instance of threading.Thread
import threading
import time

loops = [4,2]
class ThreadFun(object):
	"""docstring for ThreadFun"""
	def __init__(self, fun,args,name=''):
		self.args = args
		self.fun = fun
		self.name = name

	def __call__(self):
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
		thread = threading.Thread(target = ThreadFun(loop,(i,loops[i]),loop.__name__))
		threads.append(thread)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
	print("main end at:",time.ctime())

if __name__ == "__main__":
	main()
