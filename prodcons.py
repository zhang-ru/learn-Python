from random import randint
import time
import myThread
from queue import Queue

def writeQ(queue):
	queue.put('XXX',1)
	print('production object for Q...size now is:',queue.qsize())

def readQ(queue):
	queue.get(1)
	print('consumed object from Q...size now is:',queue.qsize())

def writer(queue,loops):
	for i in range(loops):
		writeQ(queue)
		time.sleep(randint(1,3))

def reader(queue,loops):
	for i in range(loops):
		readQ(queue)
		time.sleep(randint(2,5))

funcs = [writer,reader]
nfuncs = range(len(funcs))
def main():
	threads = []
	nloops = randint(2,5)
	q = Queue(32)
	for i in nfuncs:
		t = myThread.MyThread(funcs[i],(q,nloops),funcs[i].__name__)
		threads.append(t)

	for i in nfuncs:
		threads[i].start()
	for i in nfuncs:
		threads[i].join()
	print('all done')

if __name__ == '__main__':
	main()



