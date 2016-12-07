import re
def decodeBits(s):
	count = 1
	while True:
		b = 7*count
		m = re.search(r'1([0]{'+str(b) +'})1',s)
		if m is not None:
			t = int(len(m.group(1))/7)
			result = s.replace('0000000'*t,'   ').replace('000'*t,' ').replace('111'*t,'-').replace('1'*t,'.').replace('0'*t,'')
			return result
			break
		else: 
			count +=1

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    l = morseCode.split("   ")
    r = []
    for i in l:
        b = ""
        for s in i.split(" "):
            if MORSE_CODE.get(s.strip()) is not None:
                b = b + MORSE_CODE.get(s.strip())
        r.append(b)
    return " ".join(r).strip()

print(decodeBits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"))
'''
"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
'''
'.... . -.--   .--- ..- -.. .'


