def isPrime(number, primes):
	for i in primes:
		if number % i == 0:
			return 0
	return 1
	
	
	
def Primes(number):
	list = []
	sum = 0
	for i in range(2,number):
		if(isPrime(i, list) == 1):
			list = list + [i]
			sum += i
	print sum
	
	
Primes(2000000)
	
	
	
	
	
#print isPrime(5,[2,3])