def first_non_repeating_letter(s):
    #your code here
    t = s.upper()
    for key, val in enumerate(t):
    	if len(t.split(val)) ==2:
    		return s[key]
    		break
    	else:
    		return ''
c='stress'
a = 'stress'.upper()
for key,val in enumerate(a):
	if len(a.split(val)) ==2:
		print(c[key])
		break