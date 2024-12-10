def is_in_bounds(map, x, y):
	if y < 0 or y >= len(map):
		return 0
	if x < 0 or x >= len(map[0]):
		return 0
	return 1

def get_trail_scores(map, x, y):
	total = 0
	# print("Calling with", x, y, "height:", map[y][x])

	if map[y][x] == '9':
		map[y][x] = '.'
		return 1
	old_value = int(map[y][x])
	
	# Left
	new_pos = [x - 1, y]
	if is_in_bounds(map, new_pos[0], new_pos[1]):
		new_value = map[new_pos[1]][new_pos[0]]
		if (new_value != '.'):
			new_value = int(new_value)
			if old_value + 1 == new_value:
				total += get_trail_scores(map, new_pos[0], new_pos[1])
	
	# Down
	new_pos = [x, y + 1]
	if is_in_bounds(map, new_pos[0], new_pos[1]):
		new_value = map[new_pos[1]][new_pos[0]]
		if (new_value != '.'):
			new_value = int(new_value)
			if old_value + 1 == new_value:
				total += get_trail_scores(map, new_pos[0], new_pos[1])

	# Right
	new_pos = [x + 1, y]
	if is_in_bounds(map, new_pos[0], new_pos[1]):
		new_value = map[new_pos[1]][new_pos[0]]
		if (new_value != '.'):
			new_value = int(new_value)
			if old_value + 1 == new_value:
				total += get_trail_scores(map, new_pos[0], new_pos[1])
	
	# Up
	new_pos = [x, y - 1]
	if is_in_bounds(map, new_pos[0], new_pos[1]):
		new_value = map[new_pos[1]][new_pos[0]]
		if (new_value != '.'):
			new_value = int(new_value)
			if old_value + 1 == new_value:
				total += get_trail_scores(map, new_pos[0], new_pos[1])
	
	return total

def solve():
	with open("input.txt") as f:
		lines = f.readlines()
		map = [list(line.strip()) for line in lines]
	
	total = 0
	for y in range(len(map)):
		for x in range(len(map[0])):
			# We are starting from here
			map_copy = [row.copy() for row in map]

			if (map_copy[y][x] == '0'):
				total += get_trail_scores(map_copy, x, y)
	
	print(total)
solve()