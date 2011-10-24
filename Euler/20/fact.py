class LongInt:
  numberList = []
  def __init__(self):
    self.numberList.append(1)
  def mult(self, num):
    carry = 0
    for i in range(len(self.numberList)):
      self.numberList[i] = self.numberList[i]*num + carry
      carry = self.numberList[i] / 1000
      self.numberList[i] = self.numberList[i] % 1000
    if carry > 0:
      self.numberList.append(carry)
  
  def calcSum(self):
    total = 0
    for i in self.numberList:
      total += i / 100 + (i%100) / 10 + (i%10)
    return total




def hunFact():
  value = LongInt()
  
  for i in range(1, 101):
    value.mult(i)

  print value.calcSum()

hunFact()

