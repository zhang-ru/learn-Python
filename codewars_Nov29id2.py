def unique_in_order(iterable):
	if len(iterable) ==0:
		return []
	else:
		l = [iterable[0]]
	for i in range(len(iterable)-1):
		if iterable[i+1] != iterable[i]:
			l.append(iterable[i+1])
	return l
a = unique_in_order('AAAABBBCCDAABBB')
print(a)