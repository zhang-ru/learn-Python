def zeros(n):
    i =1
    while True:
    	if n > 5**i:
    		i+=1
    	else:
    		break
    sum = 0
    for s in range(1,i):
    	sum = sum + int(n/5**s)
    return sum

def zeros(n):
  x = int(n/5)
  return x+zeros(x) if x else 0
print(zeros(12))