def count():
	counter = 0
	for i in range(1000):
		if (i % 5 == 0) or (i % 3 == 0):
			counter += i
	print counter

count()