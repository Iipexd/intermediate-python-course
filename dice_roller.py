import random
dice_rolls = 2
def main():
  dice_sum  =  0
  for i in range (0, dice_rolls):
    roll = random.randint(1, 6)
    dice_sum += roll
    print (' Você rolou um {} '.format(roll) )
    print('Você rolou um total de ', dice_sum)

if __name__== "__main__":
  main()
