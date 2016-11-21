import time
import _thread

def loop0():
	print("loop0 start at: ", time.ctime())
	time.sleep(4)
	print("loop0 end at: ", time.ctime())
def loop1():
	print("loop1 start at: ", time.ctime())
	time.sleep(2)
	print("loop1 end at: ", time.ctime())
def main():
	print("main start at: ",time.ctime())
	_thread.start_new_thread(loop0, ())
	_thread.start_new_thread(loop1, ())
	time.sleep(6) #if missed this sentence, main function will jump to end, and loop0 and loop1 will stop immediately
	print("main end at: ",time.ctime())

if __name__ == "__main__":
	main()