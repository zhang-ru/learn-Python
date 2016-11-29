def find_even_index(arr):
    #your code here
    for i in range(len(arr)):
    	if sum(arr[:i]) == sum(arr[(i+1):]):
    		return i
    		break
    else:
    	return -1
a = find_even_index(range(1,100))
print(a)