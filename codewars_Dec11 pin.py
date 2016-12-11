import itertools
def get_pins(observed):
	l = {"1":"124",	"2":"1235",	"3":"236","4":"1457","5":"24568","6":"3569","7":"478","8":"57890","9":"689","0":"80"}
	temp = []
	result=l[observed[0]]
	if len(observed) ==1:
		return list(''.join(result))
	else:
		for i in range(1,len(observed)):
			
			result = list(itertools.product([''.join(x) for x in result],l[observed[i]],))
		return [''.join(x) for x in result]
	# return result
	# return list(itertools.product("124",['12','24']))

#ansewer:
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]

print(get_pins("8"))