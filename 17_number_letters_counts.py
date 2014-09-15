HUNDRED = len('hundred')

TENS = (
	len(''), #use index base 1, not base 0
	len(''),
	len('twenty'),
	len('thirty'),
	len('forty'),
	len('fifty'),
	len('sixty'),
	len('seventy'),
	len('eighty'),
	len('ninety'),
)

ELEVENS = (
	len('ten'),
	len('eleven'),
	len('twelve'),
	len('thirteen'),
	len('fourteen'),
	len('fifteen'),
	len('sixteen'),
	len('seventeen'),
	len('eighteen'),
	len('nineteen'),
)

ONES = (
	len(''),
	len('one'),
	len('two'),
	len('three'),
	len('four'),
	len('five'),
	len('six'),
	len('seven'),
	len('eight'),
	len('nine'),
)

total = 0

for num in range(1000):
	hundredsVal = num / 100
	tensVal = (num / 10) % 10
	onesVal = num % 10

	# word = ''
	if hundredsVal > 0:
		# word += ONES[hundredsVal] + 'hundred'
		total += ONES[hundredsVal] + HUNDRED
		if tensVal > 0 or onesVal > 0:
			# word += 'and'
			total += 3

	if tensVal == 1:
		# word += ELEVENS[onesVal]
		total += ELEVENS[onesVal]
	else:
		# word += TENS[tensVal] + ONES[onesVal]
		total += TENS[tensVal] + ONES[onesVal]
	# total += len(word)


total += len('onethousand')
print total
