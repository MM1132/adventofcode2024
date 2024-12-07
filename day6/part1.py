with open("input.txt") as f:
	lines = [[char for char in line] for line in f.read().split("\n")]

def get_tile_at_position(position):
	if (position[0] < 0 or position[0] >= len(lines[0])):
		return None
	if (position[1] < 0 or position[1] >= len(lines)):
		return None
	return lines[position[1]][position[0]]

def set_tile_at_position(position, value):
	if (position[0] < 0 or position[0] >= len(lines[0])):
		return
	if (position[1] < 0 or position[1] >= len(lines)):
		return
	lines[position[1]][position[0]] = value

def get_guard_position():
	for i, line in enumerate(lines):
		if ('^' in line):
			return [line.index('^'), i]
	return None

current_direction = "up"
while True:
	guard_position = get_guard_position()
	if (guard_position == None):
		break
	set_tile_at_position(guard_position, 'X')
	if (current_direction == "up"):
		tile_ahead = get_tile_at_position([guard_position[0], guard_position[1] - 1])
		if (tile_ahead == '#'):
			current_direction = "right"
			guard_position[0] += 1
		else:
			guard_position[1] -= 1
	elif (current_direction == "right"):
		tile_ahead = get_tile_at_position([guard_position[0] + 1, guard_position[1]])
		if (tile_ahead == '#'):
			current_direction = "down"
			guard_position[1] += 1
		else:
			guard_position[0] += 1
	elif (current_direction == "down"):
		tile_ahead = get_tile_at_position([guard_position[0], guard_position[1] + 1])
		if (tile_ahead == '#'):
			current_direction = "left"
			guard_position[0] -= 1
		else:
			guard_position[1] += 1
	elif (current_direction == "left"):
		tile_ahead = get_tile_at_position([guard_position[0] - 1, guard_position[1]])
		if (tile_ahead == '#'):
			current_direction = "up"
			guard_position[1] -= 1
		else:
			guard_position[0] -= 1
	set_tile_at_position([guard_position[0], guard_position[1]], '^')

printed_lines = "\n".join(["".join(line) for line in lines])
print(printed_lines.count('X'))

