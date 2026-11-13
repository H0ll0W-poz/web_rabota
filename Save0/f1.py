clear()
while True:
	dig()
	move(North)
	if get_pos_y() == 7:
		dig()
		move(North)
		move(East)
	