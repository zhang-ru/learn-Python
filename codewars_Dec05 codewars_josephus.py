def josephus(items,k):
	l = []
	i = 0
	while len(items) >0:
		i = (i+k-1)%len(items)
		l.append(items.pop(i))
	return l

a= josephus(["C","o","d","e","W","a","r","s"],4)
print(a)