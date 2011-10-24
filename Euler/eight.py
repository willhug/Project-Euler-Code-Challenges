import re


def largestfive():
	fin = None
	try:
		fin = open ("thousand.txt", "r")
		All = fin.read()
		Max = 0
		new = re.compile(r"[0-9]").findall(All)
		#print len(new)
		for i in range(len(new) - 4):
			mult = int(new[i]) * int(new[i+1]) * int(new[i+2]) * int(new[i+3]) * int(new[i+4])
			if(mult > Max):
				Max = mult
		print Max
				
				
				
	except IOError, e:
		print "Error in file I/O: ", e
	if fin: fin.close()
	
largestfive()