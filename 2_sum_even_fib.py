f1, f2 = 1, 2
total = 2
f3 = f1 + f2
print f3
while f3 < 4000000:
	f1, f2 = f2, f3
	f3 = f1 + f2
	print f3
	if f3 % 2 == 0:
		total += f3
		print 'total: ', total

print 'final total: ', total