while True:
	for x in range(16):
		for y in range(16):
			while get_pos_x() < x: 
				move(East)
				if can_harvest():
					harvest()
			while get_pos_x() > x: 
				move(West)
				if can_harvest():
					harvest()
			while get_pos_y() < y: 
				move(North)
				if can_harvest():
					harvest()
			while get_pos_y() > y: 
				move(South)
				if can_harvest():
					harvest()
			if (x + y) % 2 == 0:
				till()
				plant(Entities.Tree)
			if can_harvest():
					harvest()