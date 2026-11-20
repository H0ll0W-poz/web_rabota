while True:
	if get_pos_x() != 0 and get_pos_y() != 0:
		move(East)
	move(North)
	if get_pos_x() == 0 and get_pos_y() == 0:
		break
while True:
	for i in range(get_world_size()):
		if get_ground_type() != Grounds.Clay or get_ground_type() == Grounds.Dry_Rice_Terrace:
			if get_hardness() <= 3:
				dig()
				move(East)
			elif get_hardness() > 4:
				move(East)
		if get_ground_type() == Grounds.Clay:
			plant(Entities.Rice)
			move(East)
		if get_ground_type() == Grounds.Dry_Rice_Terrace:
			if can_harvest():
				harvest()
		if get_ground_type() == Grounds.Quartz:
			dig()
			move(East)
	move(North)