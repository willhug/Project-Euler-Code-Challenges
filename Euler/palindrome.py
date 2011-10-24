def ispalindrome(number):
	strnum = str(number)
	midcount = len(strnum)/2
	good = 1
	
	for i in range (midcount):
		if(strnum[i] != strnum[len(strnum) - 1 -i]):
			good = 0
	return good

def palindrome():
	largest = 1
	for i in range(100,999):
		for j in range(100,999):
			if(ispalindrome(i*j)) and (i*j > largest) :
				largest = i*j
	return largest
	
print palindrome()