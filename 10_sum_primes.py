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


total_sum = 0
MAX_NUM = 2000000
for i in range(2, MAX_NUM):
	if is_prime(i)[0] == True:
		# print 'i', i
		total_sum += i

print total_sum
