MAX_NUM = 1000
total = 0
for x in range(MAX_NUM):
	if x % 3 == 0 or x % 5 == 0:
		print x
		total += x
print total