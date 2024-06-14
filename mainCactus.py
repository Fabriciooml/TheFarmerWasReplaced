def mainCactus(n):
	counter = 0
	while True:
		if num_items(Items.Gold) < get_world_size()**2 * 10:
			mainMaze(get_world_size() * 10)
		else:
			buyItem(Items.Cactus_Seed, get_world_size()**2)
			plantCactus()
			sortCactus()
			harvest()
			if n != -1:
				counter += get_world_size()**2
			else:
				counter = -2
			if	counter >= n:
				return