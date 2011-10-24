def getEvenCase(number):
    return 2 * number

def getOddCase(number):
    if (number - 1) % 3 == 0:
        return (number - 1)/3
    return 1

def getNextValue(number):
    if(number%2==0):
        return number/2
    return number*3 + 1



valid = []

def getListOfPossibleNumbers(number):
    global valid
    
    if(number%2 == 0):
        oddBefore = getOddCase(number)
        if (oddBefore > 0 and oddBefore <= 1000000):
            return
        

    if(number%2 == 1):
        evenBefore = getEvenCase(number)
        if (evenBefore > 0 and evenBefore <= 1000000):
            return
    valid.append(number)

def getLengthTill1(number):
    count = 0
    while number != 1:
        number = getNextValue(number)
        count += 1
    return count


def findLongest():
    for i in range(1, 1000001):
           getListOfPossibleNumbers(i)
    currentLargest = 1
    currentLength = 1
    for i in valid:
        count = getLengthTill1(i)
        if(count > currentLength):
            currentLargest = i
            currentLength = count
    print currentLargest

findLongest()





