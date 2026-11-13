set_world_size(7)
def seek():
	move(North)
	for i in range(get_world_size()):
			dig()
	
	dig()
while True:
	if spawn_drone(seek):
		move(East)
	