def goTo(x, y):
	direction = East
	if get_pos_x() > x:
		direction = West
	
	while get_pos_x() != x:
		move(direction)
	
	direction = North	
	if get_pos_y() > y:
		direction = South
	
	while get_pos_y() != y:
		move(direction)