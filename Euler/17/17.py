def getDigit(digit):
    if(digit == 1 or digit == 2 or digit == 6):
        return 3
    if(digit == 4 or digit == 5 or digit == 9):
        return 4
    if(digit == 0):
        return 0
    return 5

def get10to19(number):
    if(number == 10):
        return 3
    if(number == 11 or number == 12):
       return 6
    if(number == 13 or number == 14 or number == 19 or number == 18):
       return 8
    if(number == 15 or number == 16):
       return 7
    if(number == 17):
       return 9

def getTwentyEtc(number):
    if(number == 2 or number == 3 or number == 9 or number == 8):
        return 6
    if(number == 5 or number == 6 or number == 4):
        return 5
    if(number == 7):
        return 7


def getLengthOfNumber(number):
    count = 0
    if (number == 1000):
        return 3 + 8
    if(number > 99):
      count += getDigit(number/100) + 7
       
    number = number%100
    if(count == 0):
       if(number > 19):
           count+=getTwentyEtc(number/10)
           count+=getDigit(number%10)
       elif(number < 20 and number > 9):
           count+=get10to19(number)
       else:
           count+=getDigit(number)
    elif(count > 0 and number != 0):
       count+=3
        
       if(number > 19):
           count+=getTwentyEtc(number/10)
           count+=getDigit(number%10)
       elif(number < 20 and number > 9):
           count+=get10to19(number)
       else:
           count+=getDigit(number)

    return count

def get1000():
           total = 0
           for i in range(1, 1001):
              total += getLengthOfNumber(i)
              print getLengthOfNumber(i)
           return total

print get1000()
print getLengthOfNumber(300)
print getLengthOfNumber(320)
print getLengthOfNumber(314)
print getLengthOfNumber(310)
print getLengthOfNumber(303)
