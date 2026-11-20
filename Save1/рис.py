clear()
def drone1():
	move(East)
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
		if get_pos_y() == 31:
			move(North)
			move(East)
			move(East)
def drone2():
	move(West)
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
		if get_pos_y() == 31:
			move(North)
			move(West)
			move(West)
def drone3():
	move(West)
	move(West)
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
		if get_pos_y() == 31:
			move(North)
			move(West)
			move(West)
spawn_drone(drone1)
spawn_drone(drone2)
spawn_drone(drone3)
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
	if get_pos_y() == 31:
		move(North)
		move(East)
		move(East)
		