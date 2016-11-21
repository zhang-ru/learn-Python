import re,time
from atexit import register
from urllib import request
from threading import Thread

REGX = re.compile('图书商品里排第([\d,]+)名')
Amazon = "http://www.amazon.cn/dp/"
ISBNs = {
	'0132269937': 'Core Python Programming',
	'0132356139': 'Python Web Development with Django'
	# '0137143419': 'Python Fundamentals'
}

def getRanking(isbn):
	resp = request.Request('%s%s' % (Amazon, isbn))
	resp.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36')
	resp = request.urlopen(resp)
	# if resp.getcode() == 200:
	data = resp.read().decode('utf-8')
	resp.close()
	return REGX.findall(data)[0]

def _showRanking(isbn):
	print('- %s ranked %s' % (ISBNs[isbn], getRanking(isbn)))

def _main():
	print('main start at:',time.ctime())
	for isbn in ISBNs:
		# _showRanking(isbn)
		Thread(target = _showRanking, args = (isbn,)).start() #using Thread

@register
def _atexit():
	print('all done at:', time.ctime())

if __name__ == '__main__':
	_main()