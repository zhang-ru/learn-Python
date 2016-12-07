def order_weight(strng):
    # your code
    l = strng.split()
    t=[]
    res ={}
    for i in l:
    	temp = 0
    	for j in i:
    		temp = temp+int(j)
    	res[i] = temp
    
    # return sorted(res.iteritems(), key = lambda x:x[1])

    return ' '.join(sorted(res,key = res.get))

print(order_weight("103 123 4444 202 99 2000"))


