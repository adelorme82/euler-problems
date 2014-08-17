import math
def is_prime(num):
	if num % 2 == 0 and num != 2:
		return 2, num/2
	if num % 3 == 0 and num != 3:
		return 3, num/3
	for x in range(2, int(math.floor(math.sqrt(num))) + 1):
		if num % x == 0:
			return x, num/x
	return True, num

all_factors = list()
MAX_NUM = 20
for x in range(2, MAX_NUM + 1):
	temp_factors = list()
	result = is_prime(x)
	while result[0] != True:
		temp_factors.append(result[0])
		result = is_prime(result[1])
	temp_factors.append(result[1])
	all_factors.append(temp_factors)
print all_factors

lcm = 1
for temp_list in all_factors:
	print 'temp_list:', temp_list
	for factor in temp_list:
		print 'factor:', factor
		lcm *= factor
		for remove_list in all_factors:
			print remove_list
			if factor in remove_list:
				print 'removing factor %s from list' % (factor), remove_list
				remove_list.remove(factor)
	print '================'

print lcm

