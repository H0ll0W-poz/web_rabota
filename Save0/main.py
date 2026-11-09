while True:
	if get_pos_x() == 0 and get_pos_y() == 0:
		if can_harvest():
			harvest()
			move(North)
	elif get_pos_x() == 0 and get_pos_y() == 1:
		if can_harvest():
			harvest()
			move(North)
	elif get_pos_x() == 0 and get_pos_y() == 2:
		if can_harvest():
			harvest()
			move(North)
	elif get_pos_x() == 0 and get_pos_y() == 3:
		if can_harvest():
			harvest()
			move(North)
			move(East)
	elif get_pos_x() == 1 and get_pos_y() == 0:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
	elif get_pos_x() == 1 and get_pos_y() == 1:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
	elif get_pos_x() == 1 and get_pos_y() == 2:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
	elif get_pos_x() == 1 and get_pos_y() == 3:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
			move(East)
	elif get_pos_x() == 2 and get_pos_y() == 0:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
	elif get_pos_x() == 2 and get_pos_y() == 1:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
	elif get_pos_x() == 2 and get_pos_y() == 2:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
	elif get_pos_x() == 2 and get_pos_y() == 3:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
			move(East)
	elif get_pos_x() == 3 and get_pos_y() == 0:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
	elif get_pos_x() == 3 and get_pos_y() == 1:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
	elif get_pos_x() == 3 and get_pos_y() == 2:
		if can_harvest():
			harvest()
			plant(Entities.Carrot)
			move(North)
	elif get_pos_x() == 3 and get_pos_y() == 3:
		if can_harvest():
			harvest()
			plant(Entities.Bush)
			move(North)
			move(East)