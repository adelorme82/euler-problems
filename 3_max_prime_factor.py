import math
import time
startTime = time.time()

def is_prime(num):
	if num % 2 == 0 and num != 2:
		return 2, num/2
	if num % 3 == 0 and num != 3:
		return 3, num/3
	for x in range(2, int(math.floor(math.sqrt(num))) + 1):
		if num % x == 0:
			return x, num/x
	return True, num

factors = list()
num = 600851475143  
result = is_prime(num)
print result
while result[0] != True:
	factors.append(result[0])
	result = is_prime(result[1])
	print result
factors.append(result[1])
print factors
print max(factors)

print(time.time()-startTime)
