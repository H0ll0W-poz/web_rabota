clear()
def drone1():
	move(West)
	while True:
		dig()
		move(North)
		if get_pos_y() == 31:
			dig()
			move(North)
			move(West)
			move(West)
def drone2():
	move(West)
	move(West)
	while True:
		dig()
		move(North)
		if get_pos_y() == 31:
			dig()
			move(North)
			move(West)
			move(West)
def drone3():
	move(East)
	while True:
		dig()
		move(North)
		if get_pos_y() == 31:
			dig()
			move(North)
			move(East)
			move(East)
spawn_drone(drone1)
spawn_drone(drone2)
spawn_drone(drone3)
while True:
	dig()
	move(North)
	if get_pos_y() == 31:
		dig()
		move(North)
		move(East)
		move(East)