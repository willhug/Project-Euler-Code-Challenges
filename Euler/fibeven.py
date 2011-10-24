def fibeven():
	count = 0
	fib1 = 1
	fib2 = 1
	while fib2 <= 4000000:
		if(fib2 % 2 == 0):
			count += fib2
		temp = fib2
		fib2 += fib1
		fib1 = temp
	print count

fibeven()
		