def race(v1, v2, g):
    # your code
    if v1 >= v2 :
    	return None
    else:
    	r = g/(v2-v1)
    	h = int(r)
    	mm = int((r-h)*60)
    	ss = int(((r-h)*60 - mm)*60)
    	return [h,mm,ss]