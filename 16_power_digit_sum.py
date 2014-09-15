import math
num = 2
print math.pow(2, 1000)
for x in range(1, 1000):
	num *= 2
print num

total = 0
for digit in str(num):
	total += int(digit)
print total


