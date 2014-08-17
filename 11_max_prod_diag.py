grid = [
[8, 20, 22, 97, 38, 15, 00, 40, 00, 75, 40, 5, 70, 78, 52, 12, 50, 77, 91, 8],  #0
[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 40, 56, 62, 0], #1
[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 30, 49, 13, 36, 65], #2
[52, 70, 95, 23, 40, 60, 11, 42, 69, 24, 68, 56, 10, 32, 56, 71, 37, 20, 36, 91], #3
[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], #4
[24, 47, 32, 60, 99, 30, 45, 20, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], #5
[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], #6
[67, 26, 20, 68, 20, 62, 12, 20, 95, 63, 94, 39, 63, 80, 40, 91, 66, 49, 94, 21], #7
[24, 55, 58, 50, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], #8
[21, 36, 23, 90, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95], #9
[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 30, 80, 40, 62, 16, 14, 90, 53, 56, 92], #10
[16, 39, 50, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29, 85, 57], #11
[86, 56, 00, 48, 35, 71, 89, 70, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], #12
[19, 80, 81, 68, 50, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 40, 89, 55, 40], #13
[04, 52, 80, 83, 97, 35, 99, 16, 70, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], #14
[88, 36, 68, 87, 57, 62, 20, 72, 30, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], #15
[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 80, 46, 29, 32, 40, 62, 76, 36], #16
[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 40, 36, 16], #17
[20, 73, 35, 29, 78, 31, 90, 10, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 50, 54], #18
[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 10, 89, 19, 67, 48]] #19

NUM_NUMS = 4
max_prod = 0
for row_ind in range(len(grid)):
	for col_ind in range(len(grid[row_ind])):
		#down
		if row_ind < (len(grid) - NUM_NUMS + 1):
			temp = grid[row_ind][col_ind] * grid[row_ind + 1][col_ind] * grid[row_ind + 2][col_ind] * grid[row_ind + 3][col_ind]
			if temp > max_prod:
				max_prod = temp
				print 'down new max prod'

		#right
		if col_ind < (len(grid[row_ind]) - NUM_NUMS + 1):
			temp = grid[row_ind][col_ind] * grid[row_ind][col_ind + 1] * grid[row_ind][col_ind + 2] * grid[row_ind][col_ind + 3]
			if temp > max_prod:
				max_prod = temp
				print 'right new max prod'

		#right/down
		if row_ind < (len(grid) - NUM_NUMS - 1) and col_ind < (len(grid[row_ind]) - NUM_NUMS - 1):
			temp = grid[row_ind][col_ind] * grid[row_ind + 1][col_ind + 1] * grid[row_ind + 2][col_ind + 2] * grid[row_ind + 3][col_ind + 3]
			if temp > max_prod:
				max_prod = temp
				print 'right/down new max prod'

		#right/up
		if row_ind > NUM_NUMS and col_ind < (len(grid[row_ind]) - NUM_NUMS + 1):
			temp = grid[row_ind][col_ind] * grid[row_ind - 1][col_ind + 1] * grid[row_ind - 2][col_ind + 2] * grid[row_ind - 3][col_ind + 3]
			if temp > max_prod:
				max_prod = temp
				print 'right/up new max prod'
print max_prod
