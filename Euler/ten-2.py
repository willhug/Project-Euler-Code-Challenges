def isPrime(number):
	for i in range(2,number/2 + 1):
		if(number % i == 0) and (number != i):
			return 0
	return 1



def Primes(number):
		sum = long(0)
		for i in range(2,number):
			if(isPrime(i) == 1):
				sum += i
		print sum


Primes(2000000)

#print isPrime(4)	