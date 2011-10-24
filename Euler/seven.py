def isPrime(number):
	for i in range(2,number/2 + 1):
		if(number % i == 0) and (number != i):
			return 0
	return 1


def prime(number):
	primes = 1
	i = 2
	while primes < number:
		i+=1
		if(isPrime(i)):
			primes+=1
	return i

print prime(10001)

#print isPrime(4)	