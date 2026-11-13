while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
			till()
		plant(Entities.Pumpkin)
		use_item(Items.Fertilizer)
		move(North)
	move (East)