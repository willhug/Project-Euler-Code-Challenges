from math import sqrt
from math import floor

def modreturn(Modulo, Number):
	if Number % Modulo == 0:
		return 2
	return 0

def getNumFactors (Number) :
	return sum ( [modreturn(i, Number) for i in range(1, int(sqrt(Number)))])

	

def looptriangle(numFactors):
	triangle = 1
	i = 2
	while (getNumFactors (triangle) <= numFactors):
		triangle += i
		i += 1
	return triangle
	
	
print looptriangle(500)
	