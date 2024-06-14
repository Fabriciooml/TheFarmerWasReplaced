def mainAbroba(n):
	counter = 0
	while True:
		if num_items(Items.Carrot) < get_world_size()**3:
			mainCarrot(10000)
		else:
			plantPumpkin()
			if n != -1:
				counter += get_world_size()**3
			else:
				counter = -2
		if	counter >= n:
			return
			