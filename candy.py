import time, random
from threading import Thread,BoundedSemaphore,Lock
from atexit import register

Max = 5
candy_tray = BoundedSemaphore(Max)
lock = Lock()

def refill():
	lock.acquire()
	print('filling tray')
	try:
		candy_tray.release()
	except ValueError as e:
		print("full, unable to fill")
	else:
		print("ok")
	lock.release()

def buy():
	lock.acquire()
	print("buying candy")
	if candy_tray.acquire(False):
		print('OK')
	else:
		print("empty, unable to buy")
	lock.release()

def producer(loops):
	for i in range(loops):
		refill()
		time.sleep(random.randrange(3))

def consumer(loops):
	for i in range(loops):
		buy()
		time.sleep(random.randrange(3))

def _main():
	print("starting at",time.ctime())
	nloops = random.randrange(2,6)
	print("The candy machine full with %d bars" %Max)
	Thread(target = producer, args = (nloops,)).start()
	Thread(target = consumer, args = (random.randrange(nloops,nloops+Max+2),)).start()

@register
def _atexit():
	print('all done at', time.ctime())

if __name__ =="__main__":
	_main()