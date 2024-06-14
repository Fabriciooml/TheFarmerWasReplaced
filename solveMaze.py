def solveMaze():
    aux = 0
    oldpos = [get_pos_x(),get_pos_y()]
    while get_entity_type() != Entities.Treasure:
        if aux % 4 == 0:
            up()
            if moved(oldpos[0],get_pos_x(),oldpos[1],get_pos_y()) == True:
                oldpos = [get_pos_x(),get_pos_y()]
                aux = aux+1
            else:
                aux = aux-1
        if aux % 4 == 1:
            right()
            if moved(oldpos[0],get_pos_x(),oldpos[1],get_pos_y()) == True:
                oldpos = [get_pos_x(),get_pos_y()]
                aux = aux+1
            else:
                aux = aux-1
        if aux % 4 == 2:
            down()
            if moved(oldpos[0],get_pos_x(),oldpos[1],get_pos_y()) == True:
                oldpos = [get_pos_x(),get_pos_y()]
                aux = aux+1
            else:
                aux = aux-1
        if aux % 4 == 3:
            left()
            if moved(oldpos[0],get_pos_x(),oldpos[1],get_pos_y()) == True:
                oldpos = [get_pos_x(),get_pos_y()]
                aux = aux+1
            else:
                aux = aux-1