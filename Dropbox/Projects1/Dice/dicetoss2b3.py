import random
import datetime

class DiceTwo():
   counter = 0
   occurence = 0
                  
   def __init__(self,rounds,timesPer,rollTotal):
      self.rounds = rounds
      self.timesPer = timesPer
      self.rollTotal = rollTotal
                 
      for i in range(self.rounds):
        dice1 = self.rollDice()
        dice2 = self.rollDice()
        self.counter += 1
        if dice1 + dice2 == rollTotal:
          self.occurence += 1
          #print(self.occurence)
      self.ratio1 = self.occurence/self.counter

   def rollDice(self):
        return random.choice([1,2,3,4,5,6])

   def __str__(self):
      #print('Total No. of Tests: ', self.counter)
      return 'Probability of rolling {0}: {1}'.format(self.rollTotal, self.ratio1)
      return 'Total times {0} resulted in all tests: {1}'.format(self.rollTotal, self.occurence)

timeStamp = str(datetime.datetime.now())
print('Start Time: ',timeStamp)
print()

for i in range(2,13):
   a = DiceTwo(1000,1,i)
   print(a)

print()
timeStampE = str(datetime.datetime.now())
print('End Time: ',timeStampE)



































