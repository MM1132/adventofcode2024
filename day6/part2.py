with open("input.txt") as f:
	lines_init = [[char for char in line] for line in f.read().strip().split("\n")]

class Pos:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Guard:
	def __init__(self, pos, dir):
		self.pos = pos
		self.dir = dir
	
	def move(self):
		if (self.dir == "^"):
			self.pos.y -= 1
		elif (self.dir == ">"):
			self.pos.x += 1
		elif (self.dir == "v"):
			self.pos.y += 1
		elif (self.dir == "<"):
			self.pos.x -= 1

def get_tile_at_position(pos, lines):
	if (pos.x < 0 or pos.x >= len(lines[0])):
		return None
	if (pos.y < 0 or pos.y >= len(lines)):
		return None
	return lines[pos.y][pos.x]

# Return True if we are outside the grid
def set_tile_at_position(pos, value, lines):
	if (pos.x < 0 or pos.x >= len(lines[0])):
		return True
	if (pos.y < 0 or pos.y >= len(lines)):
		return True
	lines[pos.y][pos.x] = value
	return False

def get_guard_position(lines):
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if (lines[i][j] in "^>v<"):
				return Pos(j, i)
	return None

class TurnPosition:
	def __init__(self, pos, dir):
		self.pos = pos
		self.dir = dir

# Return True if we turned successfully
def turn_guard(lines, guard):
	last_dir = guard.dir
	if (guard.dir == "^"):
		if (get_tile_at_position(Pos(guard.pos.x, guard.pos.y - 1), lines) == "#"):
			guard.dir = ">"
	elif (guard.dir == ">"):
		if (get_tile_at_position(Pos(guard.pos.x + 1, guard.pos.y), lines) == "#"):
			guard.dir = "v"
	elif (guard.dir == "v"):
		if (get_tile_at_position(Pos(guard.pos.x, guard.pos.y + 1), lines) == "#"):
			guard.dir = "<"
	elif (guard.dir == "<"):
		if (get_tile_at_position(Pos(guard.pos.x - 1, guard.pos.y), lines) == "#"):
			guard.dir = "^"
	return last_dir != guard.dir

# guard has the following format: { pos, dir }
def simulate_guard_movements(lines, guard):
	turn_list = []
	while True:

		guard.move()
		outside = set_tile_at_position(guard.pos, guard.dir, lines)
		if (outside):
			return lines

		if (guard.pos.x < 0 or guard.pos.x >= len(lines[0])):
			return lines
		if (guard.pos.y < 0 or guard.pos.y >= len(lines)):
			return lines

		previous_dir = guard.dir
		while (turn_guard(lines, guard)):
			pass
		
		# If we turned
		if (previous_dir != guard.dir):
			new_turn = TurnPosition(
				Pos(guard.pos.x, guard.pos.y),
				guard.dir
			)

			# Check if the turn position is already in the list
			for turn in turn_list:
				if turn.pos.x == new_turn.pos.x and turn.pos.y == new_turn.pos.y and turn.dir == new_turn.dir:
					return True

			turn_list.append(new_turn)

		# print("Starting: ", starting_position.x, starting_position.y, starting_direction)
		# print("Current: ", guard.pos.x, guard.pos.y, guard.dir)

counter = 0
g = get_guard_position(lines_init)
GUARD_START_X, GUARD_START_Y = g.x, g.y
starting_result = simulate_guard_movements(
	[line.copy() for line in lines_init], 
	Guard(Pos(g.x, g.y), "^")
)

# print("\n".join(["".join(line) for line in starting_result]))
# exit()
# print("#########################")

for i in range(len(lines_init)):
	for j in range(len(lines_init[0])):
		if (starting_result[i][j] in "^>v<"):
			lines_copy = [line.copy() for line in lines_init]
			lines_copy[i][j] = '#'

			new_guard = Guard(Pos(GUARD_START_X, GUARD_START_Y), "^")
			result = simulate_guard_movements(lines_copy, new_guard)
			# print("Trying at x:y... ", j, i)
			# print("\n".join(["".join(line) for line in lines_copy]))
			# exit()
			if (result == True):
				# print("Found a loop at x:y... ", j, i)
				# print("\n".join(["".join(line) for line in lines_copy]))
				# exit()
				counter += 1
				# print("New counter: ", counter)

print(counter)

# printed_lines = "\n".join(["".join(line) for line in lines_copy])
# print(printed_lines)
