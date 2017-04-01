def tictactoe():
	board=[None]+list(range(1,10))
	wincomb=[
		(1,2,3),
		(4,5,6),
		(7,8,9),
		(1,4,7),
		(2,5,8),
		(3,6,9),
		(1,5,9),
		(3,5,7),
	]

	def gameboard():
		print(board[1], board[2], board[3])
		print(board[4], board[5], board[6])
		print(board[7], board[8], board[9])
	
	def choosenum():
		while True:
			try:
				num=int(input())
				if num in board:
 					return num
				else:
					print("\nInvalid move.")
			except ValueError:
				print("\nThat's not a number.")

	def isgameover():
		for a,b,c in wincomb:
			if board[a] == board[b] == board[c]:
				print("Player {0} wins!\n".format(board[a]))
				print("Congratulations!\n")
				return True
		if sum((pos == 'X' or pos == 'O') for pos in board) == 9:
			print("TIE\n")
			return True

	for player in 'XO'*9:
		gameboard()
		if isgameover():
			break
		print("Player {0} pick your move".format(player))
		board[choosenum()] = player
		print()

while True:
	tictactoe()
	if raw_input("Want to play again? (Y/N)\n") != "Y":
		break
