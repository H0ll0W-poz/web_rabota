clear()
while True:
	while get_ground_type() != Grounds.Clay and get_entity_type() != Entities.Rice:
		dig()
		if get_ground_type() == Grounds.Rock:
			clear()
	if get_ground_type() == Grounds.Clay:
		plant(Entities.Rice)
	if get_entity_type() == Entities.Rice and can_harvest():
		harvest()
		move(North)
	if get_pos_y() == 7:
		move(North)
		move(East)