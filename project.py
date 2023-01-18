import datetime
from dateutil.relativedelta import relativedelta
import random


while True:
  player_fname = input("Enter your first name :\t")
  while(True):
    player_age = int(input("Enter your age :\t"))
    player_birthday = input("Enter your Birthday (yyyymmdd) :\t")
    year = int(player_birthday[0:4])
    month = int(player_birthday[4:6])
    day = int(player_birthday[6:8])
    player_birthday_date = datetime.datetime( year, month, day )
    today_date = datetime.datetime.now()
    years = relativedelta(
      today_date, player_birthday_date
    ).years

    if(player_age == years):
      print("Wow your age is right, let’s continue!")
      break
    else:
      print("Aha, we are in 2022 and your age is not right, kindly enter it again...")

  
  player_lucky_list=[]
  n=10
  for i in range(n):
      player_lucky_list.append(random.randint(0,200))



  count = 0

  while True:
    try:
      player_guess = int(input(f"Hi {player_fname} this is your try # {count + 1} Please enter a number between [0-200] :\t"))
      if player_guess in player_lucky_list:
        print(f"Congratulations, your lucky number is {player_guess} you got it from try # {count + 1}")
        break
      else:
        input_diff = []
        for i in player_lucky_list:
          if player_guess >=i-10 and player_guess <= i+10:
            input_diff.append(i)
        choice = input(f"your number is 10 point more or less from these numbers : {input_diff}, do you like to try again? (type ‘Y’ = yes, ‘N’ = no) :\t")
        if choice.upper() == 'N':
          break
      count += 1
    except:
      print("Sorry, wrong value, Enter a INTEGER NUMBER!!!")
  choice = input('Do you want to Play again? Yes = Y and No = N:\t')
  if choice.upper() == 'N':
    break
