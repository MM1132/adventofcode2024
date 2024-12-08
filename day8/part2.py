with open("input.txt") as f:
	lines = f.read()
	lines = [[char for char in line] for line in lines.strip().split("\n")]

WIDTH = len(lines[0])
HEIGHT = len(lines)
ANTENNA_SELECTION = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def find_all_antennas_of_type(lines, type):
	antennas = []
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] == type:
				antennas.append([x, y])
	return antennas

def calculate_inbounds_antinodes(lines, antennas):
	antinodes = []
	for antenna1 in antennas:
		for antenna2 in antennas:
			if (antenna1[0] == antenna2[0] and antenna1[1] == antenna2[1]):
				continue
			# 4 and 7
			# 4 - 3 = 1
			differenceX = antenna1[0] - antenna2[0]
			differenceY = antenna1[1] - antenna2[1]
			antinode = [antenna1[0], antenna1[1]]
			while True:
				antinode = [
					antinode[0] + (differenceX),
					antinode[1] + (differenceY)
				]
				if antinode[0] >= 0 and antinode[0] < WIDTH and antinode[1] >= 0 and antinode[1] < HEIGHT:
					antinodes.append(antinode)
				else:
					break

			differenceX = antenna2[0] - antenna1[0]
			differenceY = antenna2[1] - antenna1[1]
			antinode = [antenna1[0], antenna1[1]]
			while True:
				antinode = [
					antinode[0] + (differenceX),
					antinode[1] + (differenceY)
				]
				if antinode[0] >= 0 and antinode[0] < WIDTH and antinode[1] >= 0 and antinode[1] < HEIGHT:
					antinodes.append(antinode)
				else:
					break
	return antinodes

def get_antinodes(lines):
	antinodes = []
	for y in range(len(lines)):
		for x in range(len(lines[0])):
			if lines[y][x] in ANTENNA_SELECTION:
				antennas = find_all_antennas_of_type(lines, lines[y][x])
				for antenna in antennas:
					lines[antenna[1]][antenna[0]] = '.'
				antinode_positions = calculate_inbounds_antinodes(lines, antennas)
				for pos in antinode_positions:
					# !May be mistake
					if pos not in antinodes:
						antinodes.append(pos)

	return antinodes

antinodes = get_antinodes(lines)
print(len(antinodes))
