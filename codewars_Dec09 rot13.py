import re
def rot13(message):
    #your code here
    l=[]
    for i in message:
    	if re.search('[a-zA-Z]',i) is not None:
    		if 65<=ord(i)<78 or 97<=ord(i)<110:
    			l.append(chr(ord(i)+13))
    		else:
    			l.append(chr(ord(i)-13))
    	else:
    		l.append(i)
    return "".join(l)

a = rot13("EBG13 rknzcyr.")
print(a)
