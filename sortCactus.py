def sortCactus():
	swapsX, swapsY = 1, 1
	while swapsX and swapsY:
		swapsX, swapsY = [], []

		for yAxis in range(get_world_size()):
			for xAxis in range(get_world_size()):
								
				if measure() > measure(North) and not get_pos_y() == get_world_size() - 1:
					swap(North)
					swapsY.append(measure())
					
				if measure() > measure(East) and not get_pos_x() == get_world_size() - 1:
					swap(East)
					swapsX.append(measure())
								
				move(North)
			move(East)
