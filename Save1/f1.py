size = get_world_size()


for x in range(5):
	for y in range(5):
		while get_ground_type() != Grounds.Clay:
			dig()
		move(North)
	move(East)


while True:
	for x in range(5):
		for y in range(5):
			
			if can_harvest():
				harvest()
			
			
			if get_water() < 0.75:
				use_item(Items.Water)
			
			
			if get_ground_type() == Grounds.Clay:
				plant(Entities.Rice)
				
			while get_ground_type() == Grounds.Dry_Rice_Terrace:
				dig()
				
				
			move(North)
		move(East)
		