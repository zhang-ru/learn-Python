def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    # return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
    l = morseCode.split("   ")
    r = []
    for i in l:
    	b = ""
        for s in i.split(" "):
        	if MORSE_CODE.get(s.strip()) is not None:
        		b = b + MORSE_CODE.get(s.strip())
    	r.append(b)
    return " ".join(r).strip()
