def dig_pow(n, p):
    # your code
    l = str(n)
    sum = 0
    count = 0
    for i in range(len(l)):
    	sum= sum + int(l[i])**(p+count)
    	count = count +1
    if sum%n ==0:
    	return sum//n
    else:
    	return -1
a =dig_pow(46288, 3)
print(a)
