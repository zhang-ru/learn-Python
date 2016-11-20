import myThread
import time

def myfac(x):
	time.sleep(0.1)
	if x <2 : return 1
	return (x*fac(x-1))

def mysum(x):
	time.sleep(0.1)
	if x <2 : return 1
	return (x + sum(x-1))

def fib(x):
	time.sleep(0.005)
	if x<2: return 1
	return (fib(x-1) + fib(x-2)

func = [fib,myfac,mysum]
n = 12

def main():
	nfunc = range(len(func))
	print("single thread")
	for i in nfunc:
		print('starting', func[i]__name__,'at: ',time.ctime())
		func[i](n)
		print( func[i],'end at: ',time.ctime())

	print("multi thread")
	threads = []
	for i in nfunc:
		thread = myThread.MyThread(func[i],(n,),func[i]__name__)
		threads.append(thread)
	for i in nfunc:
		threads[i].starting()
	for i in nfunc:
		threads[i].join()
		print(threads.getResult())
	print('All finished')

if __name__ = "__main__":
	main()