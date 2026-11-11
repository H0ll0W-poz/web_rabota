
size = get_world_size()

while True:
	for y in range(size):
		for x in range(size):
			
			if can_harvest():
				harvest()
				
			if get_entity_type() == None:
				till()
				plant(Entities.Bamboo)
				
			if x < size - 1:
				move(East)
			
		if y < size - 1:
			move(North)
			
		for x in range(size - 1):
			move(West)
		