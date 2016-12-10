
def strip_url_params(url, params_to_strip = []):
    url_list = url.split("?")
    if len(url_list) == 1:
    	return url
    else:
    	l=[]
    	temp_list = url_list[1].split("&")
    	p_list = list(set(url_list[1].split("&")))
    	# p_list.sort(temp_list.index)

    	if len(params_to_strip) !=0:
    		for i in p_list:
    			for j in params_to_strip:
    				if i[0] == j:
    					p_list.remove(i)
    	for p in p_list:
    		if l.count(p[0]) == 0:
    			l.append(p[0])
    		else:
    			p_list.remove(p)
    	return url_list[0] +"?"+"&".join(p_list)
a=strip_url_params('www.codewars.com?a=1&b=2&a=2&a=1', ['b','a'])
print(a)

