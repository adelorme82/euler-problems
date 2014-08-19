import math
known_factors = {0: [None, None], 
1: [1, dict()], 
2: [2, {2:1}], 
3: [2, {3:1}],
4: [3, {2:2}],
5: [2, {5:1}],
}
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
	# print factors
	return factors

def find_factors(num):
	total = None
	count = 0
	# print 'first num', num
	for prime in range(2, int(math.floor(math.sqrt(num))) + 1):
		# print 'prime', prime
		if num % prime == 0:
			factor = num / prime
			# print 'factor', factor
			if factor % prime == 0:
				# print 'prime exists in factor'
				if not factor in known_factors:
					find_factors(factor)
				factor_tuple = known_factors[factor]
				# print 'factor_tuple', factor_tuple
				prev_total = factor_tuple[0]
				# print 'prev_total', prev_total
				# print 'factor_tuple[1]', factor_tuple[1]
				new_total = 1
				for key, value in factor_tuple[1].iteritems():
					if key != prime:
						new_total *= (1 + value)
				total = prev_total + new_total
				new_dict = dict(factor_tuple[1])
				new_dict[prime] += 1 
				known_factors[num] = [total, new_dict]
				
			else:
				# print 'new prime'
				if not factor in known_factors:
					find_factors(factor)
				total = known_factors[factor][0] * 2

				temp_dict = dict(known_factors[factor][1])
				temp_dict[prime] = 1
				known_factors[num] = [total, temp_dict]
				
			# print 'known_factors[%i]' % num, known_factors[num]
			# print 'num: %s\tcount:%i' % (num, count)
			# print '========='
			break
		else:
			count += 1
	if not total:
		known_factors[num] = [2, {num:1}]
	return total if total else 2

# print find_factors(32558400)
# print known_factors[32558400]

