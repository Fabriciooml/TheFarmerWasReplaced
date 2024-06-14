def plantHay(n):
	for i in range(n):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			right()
		up()	
	