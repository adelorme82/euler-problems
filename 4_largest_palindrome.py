pals = set()
for x in range(999,0,-1):
	for y in range(999,0,-1):
		test = x * y
		pal = str(test)
		if pal == pal[::-1]:
			print x, y, x * y
			pals.add(test)
print max(pals)



