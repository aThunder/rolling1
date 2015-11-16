
import random
import datetime
import time

def draw_ball(bucket):
    pick = (random.choice(bucket))
    return pick

def calculate(rounds):
  begin = str(datetime.datetime.now()).split('.')[0]
  match = 0
  for round in range(rounds):
    bucket = ['red','red','red','blue','blue','blue']
    selected = []

    for draw in range(3):
        counter = 0
        picked = draw_ball(bucket)
        selected.append(picked)

        for j in bucket:
         if j == picked:
            del bucket[counter]
            break
         counter += 1

    if selected[0] == selected[1] == selected[2]:
        match += 1

  print('matches: ',match)
  print('rounds: ',rounds)
  print("fraction of matches: ", (match/rounds))
  end = str(datetime.datetime.now()).split('.')[0]
  print(begin)
  print(end)

calculate(2000000)

