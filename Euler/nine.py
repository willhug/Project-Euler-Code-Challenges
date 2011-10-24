def pythag():
	for i in range(1000):
		for j in range(i):
			for k in range(j):
				if(j**2 + k**2 == i**2) and (i+j+k == 1000):
					print "numbers:", k, ",", j, ",", i, " is equal to : ", i*j*k


pythag()