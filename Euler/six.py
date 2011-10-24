def dif():
	sumsqur = 0 
	sqursum = 0
	for i in range (101):
		sumsqur += i
		sqursum += i**2
	sumsqur = sumsqur**2
	
	print sumsqur, sqursum
	
	return sumsqur - sqursum
	#	return sqursum - sumsqur
	#else:
	#	return sumsqur - sqursum


print dif()