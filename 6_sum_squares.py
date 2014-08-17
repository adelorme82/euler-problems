# sum squares
sum_squares = 0
MAX_NUM = 100
for x in range(MAX_NUM + 1):
	sum_squares = sum_squares + (x * x)
print sum_squares

total_sum = 0
for x in range(MAX_NUM + 1):
	total_sum = total_sum + x
square_sums = total_sum * total_sum
print square_sums

print square_sums - sum_squares