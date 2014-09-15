def setupMap(monthDays, year):
	# "A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400."
	isDivBy4 = year % 4 == 0
	isCentury = year % 100 == 0
	isLeapCentury = isCentury and year % 400 == 0
	monthDays[1] = 29 if (isDivBy4 and not isCentury) or (isLeapCentury) else 28

def getNextWeekday(daysInLastMonth, lastStartWeekday):
		return (lastStartWeekday + (daysInLastMonth % 7)) % 7

monthDays = {
	3 : 30,
	5 : 30,
	8 : 30,
	10 : 30,

	0 : 31,
	2 : 31,
	4 : 31,
	6 : 31,
	7 : 31,
	9 : 31,
	11 : 31,
}
days = {
	0 : 'Sunday',
	1 : 'Monday',
	2 : 'Tuesday',
	3 : 'Wednesday',
	4 : 'Thursday',
	5 : 'Friday',
	6 : 'Saturday',
}
monthNames = {
	0 : 'Jan',
	1 : 'Feb',
	2 : 'Mar',
	3 : 'Apr',
	4 : 'May',
	5 : 'Jun',
	6 : 'Jul',
	7 : 'Aug',
	8 : 'Sep',
	9 : 'Oct',
	10 : 'Nov',
	11 : 'Dec',
}
count = 0
# Jan 1 1900 was Monday
# Dec 1 1899 was Saturday
weekday = 6
for year in range(1901, 2001):
	setupMap(monthDays, year)
	for month in range(0, 12):
		lastMonth = ((month - 1) + 12) % 12
		daysInLastMonth = monthDays[lastMonth]
		weekday = getNextWeekday(daysInLastMonth, weekday)
		if weekday == 0: 
			count += 1
			print monthNames[month], year, days[weekday]

print count

