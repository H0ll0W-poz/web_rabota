def megafarm_automation():
	clear()
	
	plant(Entities.Bush)
	while get_water() < 0.9:
		use_item(Items.Water)
	while True:
		plant(Entities.Pumpkin)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
megafarm_automation()
		