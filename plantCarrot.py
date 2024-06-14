def plantCarrot(n):
	for i in range(n):
		for j in range(get_world_size()):
			if needWater():
				use_item(Items.Water_Tank)
			if can_harvest():
				harvest()
				if get_ground_type() == Grounds.Turf:
					till()
				plant(Entities.Carrots)
			right()
		up()	