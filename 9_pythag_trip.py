found = False
squares = set()
count = 1
while not found:
	print 'count: ', count
	square = count * count
	squares.add((count, square))
	for (a, a_sqr) in squares:
		for (b, b_sqr) in squares:
			if a_sqr + b_sqr == square:

				if a + b + count == 1000:
					found = True
					print a, b, count

	count += 1
