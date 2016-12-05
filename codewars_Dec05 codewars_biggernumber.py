def next_bigger(n):
    #your code here
    l = []
    for i in str(n):
    	l.append(i)
    l.sort(reverse=True)
    res = int(''.join(l))
    def sortl(n):
    	l2 = []
    	for i in str(n):
    		l2.append(i)
    	l2.sort()
    	return l2
    for a in range(n+1,res+1):
    	if sortl(a) == sortl(res):
    		return a
    else:
    	return -1

print(next_bigger(4198765432))