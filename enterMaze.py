def enterMaze():
	till()
	while get_ground_type() != Grounds.Turf:
		if num_items(Items.Fertilizer) == 0:
			if num_items(Items.Pumpkin) < 10000:
				mainAbroba(10000)
			buyItem(Items.Fertilizer, 1)
		plant(Entities.Bush)
		use_item(Items.Fertilizer)
	solveMaze()
	harvest()