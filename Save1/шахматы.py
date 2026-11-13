def do_farm(offset):
	while True:
		for y in range(offset, get_world_size(), 3):
			for x in range(get_world_size()):
				while get_pos_x() != x:
					move(East)
				while get_pos_y() != y:
					move(North)
				if (x + y) % 2 == 0:
					if can_harvest():
						harvest()
					plant(Entities.Tree)
					use_item(Items.Water)
			
				else:
					if can_harvest():
						harvest()
			
def drone_0_task():
	do_farm(0)
def drone_1_task():
	do_farm(1)
def drone_2_task():
	do_farm(2)
def drone_3_task():
	do_farm(3)
def drone_4_task():
	do_farm(4)
def drone_5_task():
	do_farm(5)
def drone_6_task():
	do_farm(6)
def drone_7_task():
	do_farm(7)
def drone_8_task():
	do_farm(8)
spawn_drone(drone_0_task)
spawn_drone(drone_1_task)
spawn_drone(drone_2_task)
spawn_drone(drone_3_task)
spawn_drone(drone_4_task)
spawn_drone(drone_5_task)
spawn_drone(drone_6_task)
spawn_drone(drone_7_task)
spawn_drone(drone_8_task)
