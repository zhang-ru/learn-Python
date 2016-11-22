import time
from random import randrange
from atexit import register
from threading import Thread,Lock,currentThread

class CleanOutputSet(set):
	"""docstring for CleanOutputSet"""
	def __str__(self):
		return ', '.join(x for x in self)
		

lock = Lock()
#prived a list from 2 to 4 for 3-6 times
neconds = (randrange(2,5) for x in range(randrange(3,7)))
# instance 
remains = CleanOutputSet()

def loop(nsec):
	myname = currentThread().name
	lock.acquire()
	remains.add(myname)
	print('[%s] started %s' %(time.ctime(), myname))
	lock.release()
	time.sleep(nsec)
	# lock.acquire()
	remains.remove(myname)
	print('[%s] completed at %s' %(time.ctime(), myname))
	print('remaining: %s' %(remains or 'None'))
	# lock.release()

def _main():
	for secnds in neconds:
		Thread(target = loop, args = (secnds,)).start()

@register
def _atexit():
	print('all done at', time.ctime())

if __name__ == '__main__':
	_main()