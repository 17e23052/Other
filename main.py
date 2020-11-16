from random import randrange
dice_1 = randrange(1,7)
dice_2 = randrange(1,7)
if dice_1 == 1 or dice_1 == 3 or dice_1 == 5:
  print(f"You rolled a {dice_1} which is odd")
elif dice_1 == 2 or dice_1 == 4 or dice_1 == 6:
  print(f"You rolled a {dice_1} which is even")
if dice_2 == 1 or dice_2 == 3 or dice_2 == 5:
  print(f"You rolled a {dice_2} which is odd")
elif dice_2 == 2 or dice_2 == 4 or dice_2 == 6:
  print(f"You rolled a {dice_2} which is even")
if dice_1 == dice_2:
  print("You rolled a double!")
else:
  print("You did not roll a double.")