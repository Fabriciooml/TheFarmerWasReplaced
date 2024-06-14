def plantBush(n):
	for i in range(n):
		for j in range(get_world_size()):
			if get_entity_type() == None:
				plant(Entities.Bush)
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			right()
		up()