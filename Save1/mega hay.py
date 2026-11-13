def harvest_column():
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		move(North)

while True:
	if spawn_drone(harvest_column):
		move(East)