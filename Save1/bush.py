while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		plant(Entities.Bush)
		use_item(Items.Fertilizer)
		move(North)
	move (East)