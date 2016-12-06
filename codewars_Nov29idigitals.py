def square_digits(num):
    s = str(num)
    l = []
    for i,v in enumerate(s):
    	l.append(str(int(v)**2))
    return int(''.join(l))
a = square_digits(9119)
print(a)