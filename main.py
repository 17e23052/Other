from random import randrange
dice_1 = randrange(1,7)
dice_2 = randrange(1,7)
print(f"You rolled a {dice_1} and a {dice_2}")
if dice_1 == dice_2:
  print("You rolled a double!")
else:
  print("You did not roll a double.")