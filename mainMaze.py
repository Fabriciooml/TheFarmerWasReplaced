def mainMaze(n):
	counter = 0
	while True:
		enterMaze()
		if n != -1:
			counter += 1
		else:
			counter = -2
		if	counter >= n:
			return