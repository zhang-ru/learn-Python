import re,math
def going_my(n):
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
def going(n):
    factor = 1.0
    acc = 1.0
    for i in range(n, 1, -1):
        factor *= 1.0 / i
        acc += factor
    return int(acc * 1e6) / 1e6

def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6
    
print(going(4))