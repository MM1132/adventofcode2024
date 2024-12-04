import re

with open("input.txt") as f:
	lines = f.readlines()
def contains_xmas(word):
	return word == "XMAS" or word == "SAMX"

horizontal_count = 0
vertical_count = 0
diagonal_count = 0
diagonal_other_count = 0
for y in range(len(lines)):
	for x in range(len(lines[0].strip())):
		# Horizontal
		if x <= len(lines[0].strip()) - 1 - 3:
			word = ""
			for i in range(4):
				word += lines[y][x + i]
			if contains_xmas(word):
				horizontal_count += 1
		
		# Vertical
		if y <= len(lines) - 1 - 3:
			word = ""
			for i in range(4):
				word += lines[y + i][x]
			if contains_xmas(word):
				vertical_count += 1

		# Diagonal
		if y <= len(lines) - 1 - 3 and x <= len(lines[0].strip()) - 1 - 3:
			word = ""
			for i in range(4):
				word += lines[y + i][x + i]
			if contains_xmas(word):
				diagonal_count += 1
		# Diagonal other
		if y >= 3 and x <= len(lines[0].strip()) - 1 - 3:
			word = ""
			for i in range(4):
				word += lines[y - i][x + i]
			if contains_xmas(word):
				diagonal_other_count += 1

print(horizontal_count + vertical_count + diagonal_count + diagonal_other_count)
# Print separately
print(horizontal_count)
print(vertical_count)
print(diagonal_count)
print(diagonal_other_count)
