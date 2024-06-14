#Work in progress

def getCactusMatrix():
	matrix = []
	for i in range(get_world_size()):
		matrix.append([])
		for j in range(get_world_size()):
			matrix[i].append(measure())
			right()
		up()
	return matrix

def swapCactusX(newPosition):
	pos = get_pos_x()
	
	direction = East
	if pos > newPosition:
		direction = West
	if get_pos_x() == newPosition:
		return
	while get_pos_x() != newPosition:
		swap(direction)
		move(direction)
	
	direction = West
	if pos > get_pos_x():
		direction = East
	
	move(direction)
	
	while get_pos_x() != pos:
		swap(direction)
		move(direction)
		

def partitionX(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            goTo(i, get_pos_y())
         
            swapCactusX(j)
            
            (array[i], array[j]) = (array[j], array[i])
    goTo(i + 1, get_pos_y())
    swapCactusX(high)
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def swapCactusY(newPosition):
	pos = get_pos_y()
	
	direction = North
	if pos > newPosition:
		direction = South
	if get_pos_y() == newPosition:
		return
	while get_pos_y() != newPosition:
		swap(direction)
		move(direction)
	
	direction = South
	if pos > get_pos_x():
		direction = North
	
	move(direction)
	
	while get_pos_y() != pos:
		swap(direction)
		move(direction)
		

def partitionY(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            goTo(get_pos_x(), j)
         
            swapCactusY(i)
            
            (array[i], array[j]) = (array[j], array[i])
    goTo(get_pos_x(), high)
    swapCactusY(i + 1)
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high, is_line):
    if low < high:
		
		if is_line:
			pi = partitionX(array, low, high)
		else:
			pi = partitionY(array, low, high)
		quickSort(array, low, pi - 1, is_line)
		quickSort(array, pi + 1, high, is_line)

        

def quickSortCactus():
	goTo(0,0)
	cactusMatrix = getCactusMatrix()
	for line in cactusMatrix:
		
		quickSort(line, 0, get_world_size() - 1, True)
		
		if get_pos_y() + 1 != get_world_size():
			goTo(0, get_pos_y() + 1)
		else:
			goTo(0,0)
	
	cactusMatrix = getCactusMatrix()
	columns = []
	for i in range(get_world_size()):
		columns.append([])
		for row in cactusMatrix:
			columns[i].append(row[i])
	
	for column in columns:
		#print(column)
		
		quickSort(column, 0, get_world_size() - 1, False)
		
		if get_pos_x() + 1 != get_world_size():
			goTo(get_pos_x() + 1, 0)
		else:
			goTo(0,0)
