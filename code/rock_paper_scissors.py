#'Probably overcomplicated' code for a game of rock, paper, scissors - oh well
import random,os

running = True
moves = ("r","p","s")

wins = 0
losses = 0
draws = 0

max_games = 1
current_game_count = 0

def ClearScreen():
	if os.name == "nt":os.system("cls")
	else:os.system("clear")

def Prompt(display_str):
	i = input(display_str)
	i = i.lower()
	return i

def Score(r_str):
	global wins,losses,draws
	if r_str == "w":wins += 1
	if r_str == "l":losses += 1
	if r_str == "d":draws += 1

while running:
	ClearScreen()
	print("Welcome to Rock Paper Scissors.")
	while current_game_count < max_games:
		if max_games == 1:
			max_games = Prompt("Enter number of rounds to play: ")
			if max_games.isdigit():
				if int(max_games) > 25:
					ClearScreen()
					print(f"{max_games} rounds is a bit much, don't ya think? Try again.")
					max_games = 1
					continue
			else:
				ClearScreen()
				print("Not a number. Try again.")
				max_games = 1
				continue
			max_games = int(max_games)
			ClearScreen()
		
		print(f"Round {current_game_count+1}...")
		user_move = Prompt("Please enter your move (r,p,s): ")
		if user_move not in moves or len(user_move) > 1:
			ClearScreen()
			print("Not a valid move. Try again.")
			continue
		
		cpu_move = random.choice(moves)
		
		ClearScreen()
		if user_move == "r":
			if cpu_move == "r":
				print("You chose Rock and the computer chose Rock. It's a DRAW?")
				Score("d")
			elif cpu_move == "p":
				print("You chose Rock and the computer chose Paper. It's a LOSS.")
				Score("l")
			else:
				print("You chose Rock and the computer chose Scissors. It's a WIN!")
				Score("w")
		if user_move == "p":
			if cpu_move == "r":
				print("You chose Paper and the computer chose Rock. It's a WIN!")
				Score("w")
			elif cpu_move == "p":
				print("You chose Paper and the computer chose Paper. It's a DRAW?")
				Score("d")
			else:
				print("You chose Paper and the computer chose Scissors. It's a LOSS.")
				Score("l")
		if user_move == "s":
			if cpu_move == "r":
				print("You chose Scissors and the computer chose Rock. It's a LOSS.")
				Score("l")
			elif cpu_move == "p":
				print("You chose Scissors and the computer chose Paper. It's a WIN!")
				Score("w")
			else:
				print("You chose Scissors and the computer chose Scissors. It's a DRAW?")
				Score("d")

		current_game_count += 1

	print(f"Game Over. Wins: {wins} | Losses: {losses} | Draws: {draws}")
	wins = 0
	losses = 0
	draws = 0

	inp = Prompt("Play again? (Y/N): ")
	if inp == "y":
		current_game_count = 0
		max_games = 1
	else:break