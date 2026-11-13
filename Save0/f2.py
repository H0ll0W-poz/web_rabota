clear()
while True:
	
	direction = prospect_iron()
	
	if direction == None:
		dig()
		
	else:
		move(direction)