clear()
def worker(lane):
	size = get_world_size()
	
	while get_pos_x() > 0:
		move(West)
		
	for _ in range(lane):
		move(East)
		
	while True:
		for col in range(4):
			for row in range(size):
					
				while get_ground_type() != Grounds.Clay and get_entity_type() != Entities.Rice:
					dig()
					if get_ground_type() == Grounds.Rock:
						clear()

				if get_ground_type() == Grounds.Clay:
					plant(Entities.Rice)
				
				if get_entity_type() == Entities.Rice and can_harvest():
					harvest()
					move(North)
					
				if row < size - 1:
					move(North)
					
			if col < 3:
				for _ in range(8):
					move(East)
			
for i in range(1, 8):
	spawn_drone(worker, i)
	
worker(0)