import time

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
	loop0()
	loop1()
	print("main end at: ",time.ctime())

if __name__ == "__main__":
	main()