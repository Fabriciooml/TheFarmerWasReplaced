def plantCactus():
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			till()
			plant(Entities.Cactus)
			right()
		up()
			