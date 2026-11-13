while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			till()
		plant(Entities.Sunflower)
		move(North)
	move (East)