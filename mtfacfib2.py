import time, myThread

def fib(x):
	time.sleep(0.005)
	if x<2: return 1
	return (fib(x-1) + fib(x-2))

def fac(x):
	time.sleep(0.1)
	if x<2: return 1
	return (fac(x-1) * x)

def sum(x):
	time.sleep(0.1)
	if x<2: return 1
	return (x + sum(x-1))

funcs = [fib,fac,sum]
n = 12

def main():
	nfunc = range(len(funcs))
	print("single thread")
	for i in nfunc:
		print('starting', funcs[i].__name__,'at: ',time.ctime())
		funcs[i](n)
		print(funcs[i](n))
		print( funcs[i],'end at: ',time.ctime())

	print("multi thread")
	threads = []
	for i in nfunc:
		thread = myThread.MyThread(funcs[i],(n,),funcs[i].__name__)
		threads.append(thread)
	for i in nfunc:
		threads[i].start()
	for i in nfunc:
		threads[i].join()
		print(threads[i].getResult())
	print('All finished')

if __name__ == "__main__":
	main()