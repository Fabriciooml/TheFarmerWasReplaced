def plantSunflower():
    aux = 0
    while True:
        
        buyItem(Items.Sunflower_Seed, get_world_size()**2)
        if aux == 0:
            clear()
        petalas = 0
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if aux == 0:
                    till()
                
                plant(Entities.Sunflower)
                while needWater():
					use_item(Items.Water_Tank)                    
                right()
            up()
        aux = 1
        maisPetalas = find_strong()
        for k in range (maisPetalas-6):
            for i in range(get_world_size()):
                for j in range(get_world_size()):
                    if measure() == maisPetalas-k:
						if can_harvest():
							harvest()
                    right()
                up()
        break