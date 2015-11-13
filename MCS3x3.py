
import random

def draw_ball(bucket):
    pick = (random.choice(bucket))
    return pick

def calculate(rounds):
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

    # print("bucket: ", bucket)
    # print("selected: ",selected)

    if selected[0] == selected[1] == selected[2]:
        match += 1

  print('matches: ',match)
  print('rounds: ',rounds)
  fraction = match/rounds
  print("fraction of matches: ", fraction)

calculate(200000)

