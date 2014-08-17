import math
def is_prime(num):
	# print num, int(math.ceil(math.sqrt(num)))
	for x in range(2, int(math.floor(math.sqrt(num))) + 1):
		# print 'x', x
		# print num % x
		if num % x == 0:
			# print 'False'
			return False
	# print '====='
	return True

MAX_NUM = 10001
num_primes = 0
x = 2
prime = 0
while num_primes < MAX_NUM:
	if is_prime(x):
		num_primes = num_primes + 1
		print x, 'is prime number', num_primes
		prime = x
	x = x + 1
print prime

