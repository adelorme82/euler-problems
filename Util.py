import math
# @return a tuple, first value is either true or 
def is_prime(num):
	if num % 2 == 0 and num != 2:
		return 2, num/2
	if num % 3 == 0 and num != 3:
		return 3, num/3
	for x in range(2, int(math.floor(math.sqrt(num))) + 1):
		if num % x == 0:
			return x, num/x
	return True, num

# @return prime factors in list
def find_prime_factors(num):
	factors = list()
	result = is_prime(num)
	# print 'result: ', result
	while result[0] != True and result[0] != result[1]:
		factors.append(result[0])
		result = is_prime(result[1])
	# 	print result
	factors.append(result[1])
	print factors
	return factors

def find_factors(num):
	factors = {1}
	# print num, (num + 1/2)/2
	for x in range(1, (num + 1/2)/2 + 1):
		if num % x == 0:
			factors.add(x)
			factors.add(num/x)
	return factors

