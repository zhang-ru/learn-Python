def make_readable(seconds):
    # Do something
    if seconds > 359999 : return None
    else:
        hh = int(seconds/3600)
        mm = int((seconds-hh*3600)/60)
        ss = seconds%60
        def twodigital(n):
        	if n <10:
        		return "0"+str(n)
        	else:
        		return str(n)
        return twodigital(hh)+":"+twodigital(mm)+":"+twodigital(ss)
a = make_readable(0)
print(a)