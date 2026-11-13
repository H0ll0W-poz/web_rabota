clear()
size = get_world_size()
for row in range(size):
	for col in range(size):
		if get_ground_type() != Grounds.Soil:
			till()
		move(North)
	move(East)
while True:
	for row in range(size):
		for col in range(size):
		
			if can_harvest():
				harvest()
			
			if get_entity_type() == None:
				plant(Entities.Bamboo)
			
			move(North)
		
		move(East)