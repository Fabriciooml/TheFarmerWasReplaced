def plantPumpkin():
	while True:
		pumpkin_counter = 0
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_ground_type() == Grounds.Turf:
					till()
				if get_entity_type() == Entities.Pumpkin:
					pumpkin_counter += 1
				elif get_entity_type() == Entities.Bush:
					harvest()
					
				else:
					buyItem(Items.Pumpkin_Seed, 1)
					if needWater():
						use_item(Items.Water_Tank)
					plant(Entities.Pumpkin)
				right()
			up()
			if pumpkin_counter == get_world_size()**2:
				harvest()
				return