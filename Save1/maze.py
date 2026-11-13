def spawn_maze():
	if get_ground_type() != Grounds.Soil:
		till()
	harvest()
	plant(Entities.Bush)
	size = get_world_size()
	use_item(Items.Weird_Substance, size)
def solve_maze():
	dirs = [North, East, South, West]
	facing =  0 # 0 - North, 1 - East, 2 -South, 3 - West
	
	while get_entity_type() != Entities.Treasure:
		left = (facing - 1) % 4
		if can_move(dirs[left]):
			facing = left
			move(dirs[left])
		elif can_move(dirs[facing]):
			move(dirs[facing])
		else:
			facing = (facing + 1) % 4
while True:
	spawn_maze()
	solve_maze()