import re,math
def going(n):
    sum =0
    for i in range(1,n+1):
    	sum = sum + math.factorial(i)
    result = sum/math.factorial(n)
    f = re.search(r'\.([\d]*)',str(result))
    # print(result)
    if len(f.group(1)) <7:
    	return result
    else:
    	return math.floor(result*1000000)/1000000

print(going(81))