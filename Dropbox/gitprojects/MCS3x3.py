
import random

def draw_ball(bucket):
    pick = (random.choice(bucket))
    # print(pick)
    # print(bucket)
    return pick

def calculate(rounds):
  match = 0
  for round in range(rounds):
    bucket = ['red','red','red','blue','blue','blue']
    selected = []

    for draw in range(3):
        # print(bucket)
        counter = 0
        pick = draw_ball(bucket)
        selected.append(pick)

        for j in bucket:
         if j == pick:
            # print("hello", j)
            del bucket[counter]
            break
         counter += 1

    # print("bucket: ", bucket)
    # print("selected: ",selected)

    if selected[0] == selected[1] == selected[2]:
        # print("yes")
        match += 1
        # print(match)

  print('matches: ',match)
  print('rounds: ',rounds)
  fraction = match/rounds
  print("fraction of matches: ", fraction)


calculate(20000)

