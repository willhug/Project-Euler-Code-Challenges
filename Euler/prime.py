def large(number):
	largest = 1
	iterator = number
	i = 2
	while iterator != 1:
		while (iterator % i == 0):
			largest = i
			iterator /= i
		i += 1
	print largest

large (600851475143)
			