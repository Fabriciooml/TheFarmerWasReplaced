def find_strong():
    petalas = 0
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if measure() > petalas:
                posMaisPetalas=[get_pos_x(),get_pos_y()]
                petalas=measure()
            right()
        up()
    return petalas