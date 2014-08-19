import Util
import time
startTime = time.time()

MAX_DIVISORS = 500
triangle = 0
divisors = 0
count = 6
while divisors < MAX_DIVISORS:
	triangle += count
	print triangle
	count += 1
	divisors = Util.find_factors(triangle)
	if divisors > 100:
		print triangle, count, divisors
	# print '======'
print triangle

print(time.time()-startTime)
# for number, details in Util.known_factors.iteritems():
# 	print number, details[0]
# 	print details[1]
# 	print '============'





print(32534196 - 32526130)
print(32542263 - 32534196)
print(32550331 - 32542263)
print(32558400 - 32550331)