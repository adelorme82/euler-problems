import Util


MAX_DIVISORS = 500
triangle = 0
divisors = 0
count = 1
while divisors < MAX_DIVISORS:
	triangle += count
	# print triangle
	count += 1
	divisors = len(Util.find_factors(triangle))
	if divisors > 100:
		print triangle, count, divisors
	# print '======'
print triangle




