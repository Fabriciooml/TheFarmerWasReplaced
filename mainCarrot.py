def mainCarrot(n):
	counter = 0
	while True:
		if num_items(Items.Carrot_Seed) >= get_world_size()**2:
			plantCarrot(get_world_size())
			if n != -1:
				counter += get_world_size()**2
			else:
				counter = -2
		elif num_items(Items.Wood) < 10000 or num_items(Items.Hay) < 10000:
			plantBush(get_world_size()**3)
			plantHay(get_world_size()**3)
		else:
			#plantBush(get_world_size()**3)
			#plantHay(get_world_size()**3)
			buyItem(Items.Empty_Tank, 1)
			buyItem(Items.Carrot_Seed, get_world_size()**2)
		if	counter >= n:
			return