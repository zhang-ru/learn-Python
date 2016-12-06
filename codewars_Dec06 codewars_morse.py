import re
def decodeBits(bits):
	count = 1
	while True:
		b = 7*count
		m = re.search(r'1([0]{'+str(b) +'})1',bits)
		if m is not None:
			return int(len(m.group(1))/7)
			break
		else: 
			count +=1
print(decodeBits("1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"))
# a = "1111110000000000000011"
# b=14
# m = re.search('1([0]{'+str(b)+'})1',a)
# print(m.group(1))