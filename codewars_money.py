def calculate_years(principal, interest, tax, desired):
    # raise NotImplementedError("TODO: calculate_years")
    if principal > desired: return 0
    else:
    	count = 0
    	new_sum = principal
    	while new_sum < desired:
    		new_sum = (1+interest)*new_sum - new_sum*interest*tax
    		count = count + 1

    	return count

b = calculate_years(1000, 0.01625, 0.18,1200)
print(b)