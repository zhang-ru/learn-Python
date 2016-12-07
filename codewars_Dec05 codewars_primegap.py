import math
def gap(g, m, n):
    # your code
    l=[]
    for i in range(m,n+1):
    	for j in range(2,int(math.sqrt(i))+1):
    		if i%j ==0:
    			break
    	else:
    		l.append(i)

    for i in range(1,len(l)):
    	if (l[i] - l[i-1]) == g :
    		return [l[i-1],l[i]]
    		break
    	else:
    		continue

print(gap(8,300,400))


