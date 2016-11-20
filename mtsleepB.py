import time, _thread

loops = [4,2] #define array of waiting senconds

# define loop function, including three args: ID of loop, waiting seconds, lock object
def loop(nloop,nsec,lock):
	print('loop',nloop,'start at: ',time.ctime())
	time.sleep(nsec)
	print('loop',nloop,'end at: ',time.ctime())
	lock.release() #release the lock after function close

def main():
	print('main start at: ',time.ctime())
	nloops = range(len(loops))

	#create locks
	locks = []
	for i in nloops:
		lock = _thread.allocate_lock()
		lock.acquire()
		locks.append(lock)
	#create loop using thread
	for i in nloops:
		_thread.start_new_thread(loop,(i,loops[i],locks[i]))
	#check the lock status
	for i in nloops:
		while locks[i].locked():
			pass


	print('main end at: ',time.ctime())


if __name__ == "__main__":
	main()

