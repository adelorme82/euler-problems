import Util
import time
startTime = time.time()

MAX_DIVISORS = 500
triangle = 0
divisors = 0
count = 1
while divisors < MAX_DIVISORS:
	triangle += count
	# print triangle
	count += 1
	divisors = Util.find_factors(triangle)
	# if divisors > 100:
		# print triangle, count, divisors
	# print '======'
print 'triangle', triangle

print(time.time()-startTime)
# for number, details in Util.known_factors.iteritems():
# 	print number, details[0]
# 	print details[1]
# 	print '============'
print Util.known_factors[triangle][1]



