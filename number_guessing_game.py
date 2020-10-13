#A number guessing game in the console. Select your difficulty and guess a number till your score goes to zero.
import random,os
def Game():
  ClearScreen()
  d = {"Easy":(1,10),"Hard":(1,100),"Nice":(69,420),"Leet":(0,1337),"Random":tuple(sorted([random.randint(0,9999) for _ in range(2)]))}
  print("Number guessing game!\n\nChoose your difficulty:\n")
  print("\n".join(map(lambda x: str(list(d.keys()).index(x)+1)+") - "+x,d.keys())))
  score = 10
  prev_guess = -1
  choice = NumberPrompt("",1,len(d)) - 1
  min_n = d.get(list(d.keys())[choice])[0]
  max_n = d.get(list(d.keys())[choice])[1]
  number = random.randint(min_n,max_n)
  hints = ["You're not even trying, are you?","You're on fire!","You're hot!","You're getting warmer!","You're getting cooler.","You're cold.","You're ice.","Keep trying!"]
  clues = [f"The number is {len(str(number))} digit{'s' if number>1 else ''} long.",f"The number is {(lambda x: 'greater than '+str(x) if number>x else 'less than '+str(x))(random.randint(min_n,max_n))}",f"The number is {(lambda x: 'greater than '+str(x) if number>x else 'less than '+str(x))(random.randint(min_n,max_n))}",f"The number is {(lambda x: 'greater than '+str(x) if number>x else 'less than '+str(x))(random.randint(min_n,max_n))}",f"The number is {'even' if number%2==0 else 'odd'}",f"The number is divisible by {random.choice(list(filter(lambda x: (number%x==0 and x!=1), [n for n in range(1,number+1)]))) if number!=0 else [0]}",f"The number is divisible by {random.choice(list(filter(lambda x: (number%x==0 and x!=1), [n for n in range(1,number+1)]))) if number!=0 else [0]}",f"The number ends with {str(number)[-1]}"]
  ClearScreen()
  while True:
    guess = NumberPrompt(f"I am thinking of a number between {min_n} and {max_n}...\nWhat number am I thinking of?\n")
    ClearScreen()
    if guess == number:
      print(f"Correct! {number} was the number! You win!\nScore: {score}\n")
      GameOver()
      break
    else:
      difference = abs(number - guess)
      if guess > max_n or guess < min_n: h = 0
      elif difference < 3: h = 1
      elif difference < 6: h = 2
      elif difference > max_n // 2: h = 6
      elif difference > max_n // 3: h = 5
      elif difference > abs(number - prev_guess) and prev_guess != -1: h = 4
      elif difference < abs(number - prev_guess) and prev_guess != -1: h = 3
      else: h = 7
      score -= 1
      prev_guess = guess
      print(f"{guess} is incorrect! - {hints[h]}\nHere's a clue: {clues[random.randint(0,len(clues)-1)]}\nScore: {score}\n")
      if score <= 0:
        GameOver()
        break
def GameOver():
  again = input("Game Over\nPlay again?(Y/N)\n")
  if again.upper() == "Y": Game()
def NumberPrompt(prompt:str,min_range:int=-1,max_range:int=-1):
  while True:
    k = input(prompt)
    if not k.isdigit(): print("Invalid")
    elif min_range != -1 and max_range != -1:
      if int(k) not in list(range(min_range,max_range+1)): print("Invalid Number")
      else: return int(k)
    else: break
  return int(k)
def ClearScreen():
  os.system("cls") if os.name == "nt" else os.system("clear")
Game()