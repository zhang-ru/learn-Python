import threading
import time

loops = [4,2]
def loop(nloop,nsecd):
	print('loop',nloop,'start at: ',time.ctime())
	time.sleep(nsecd)
	print('loop',nloop,'end at: ',time.ctime())

def main():
	print("main start at:",time.ctime())
	nloops = range(len(loops))
	threads = []
	for i in nloops:
		thread = threading.Thread(target = loop, args = (i,loops[i]))
		threads.append(thread)
	for i in nloops:
		threads[i].start()
	for i in nloops:
		threads[i].join()
	print("main end at:",time.ctime())

if __name__ == "__main__":
	main()

