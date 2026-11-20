while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_x() % 2 == 0:
				if get_water() < 0.25:
					use_item(Items.Water)
				plant(Entities.Tree)
				move(East)
			else:
				if get_ground_type() == Grounds.Grassland:
					if get_water() < 0.25:
						use_item (Items.Water)
					till()
					plant(Entities.Carrot)
					move(East)
				else:
					if get_water() < 0.25:
						use_item(Items.Water)
					plant(Entities.Carrot)
					move(East)
	move(North)
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			if get_pos_x() % 2 != 0:
				if get_water() < 0.25:
					use_item(Items.Water)
				plant(Entities.Tree)
				move(East)
			else:
				plant(Entities.Grass)
				move(East)
	move(North)

					
			
		