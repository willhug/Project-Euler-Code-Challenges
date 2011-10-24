import sys

  

def sumhundred ():
	Lines = open("hundred.txt")
        number = 0
	for Line in Lines.readlines():
                #for each number, add it to a global Number type
		num = []
		for i in range(0, 50):
                  number += (int(Line[i])) * pow(10, (50 - i))
			#num.append(int(Line[i]))
		print number

sumhundred()
#print range(50,0,-1)
