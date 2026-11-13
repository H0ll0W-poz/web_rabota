W = get_world_size()

# Вернуться домой
def go_home():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

# Полить текущую клетку
def water_here():
	if get_water() < 100:
		use_item(Items.Water)

# Посадить кактус
def plant_here():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)
	water_here()

# Пройти всё поле и сделать действие на каждой клетке
def walk_field(action):
	go_home()
	for y in range(W):
		for x in range(W):
			action()
			if x < W - 1:
				move(East)
		if y < W - 1:
			move(North)
			while get_pos_x() > 0:
				move(West)

# Один проход сортировки — всегда слева направо, снизу вверх
def sort_pass():
	go_home()
	swapped = False
	for y in range(W):
		for x in range(W):
			# Сравниваем с соседом справа (East)
			if x < W - 1:
				if measure() > measure(East):
					swap(East)
					swapped = True
			# Сравниваем с соседом сверху (North)
			if y < W - 1:
				if measure() > measure(North):
					swap(North)
					swapped = True
			if x < W - 1:
				move(East)
		if y < W - 1:
			move(North)
			while get_pos_x() > 0:
				move(West)
	return swapped

# Проверить: всё созрело?
def all_ready():
	go_home()
	for y in range(W):
		for x in range(W):
			if not can_harvest():
				return False
			if x < W - 1:
				move(East)
		if y < W - 1:
			move(North)
			while get_pos_x() > 0:
				move(West)
	return True

# Полить всё поле
def water_all():
	go_home()
	for y in range(W):
		for x in range(W):
			water_here()
			if x < W - 1:
				move(East)
		if y < W - 1:
			move(North)
			while get_pos_x() > 0:
				move(West)

# === ГЛАВНЫЙ ЦИКЛ ===
walk_field(plant_here)

while True:
	# Ждём созревания, поливая поле
	while not all_ready():
		water_all()
	
	# Сортируем, пока не будет ни одного обмена
	while sort_pass():
		pass
	
	# Собираем — один harvest соберёт весь квадрат
	go_home()
	harvest()
	
	# Снова сажаем
	walk_field(plant_here)
	