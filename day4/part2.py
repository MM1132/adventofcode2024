import re

with open("input.txt") as f:
	lines = f.readlines()
def contains_mas(word):
	return word == "MAS" or word == "SAM"

xcount = 0
for y in range(1, len(lines) - 1):
	for x in range(1, len(lines[0].strip()) - 1):
		first = lines[y - 1][x - 1] + lines[y][x] + lines[y + 1][x + 1]
		second = lines[y + 1][x - 1] + lines[y][x] + lines[y - 1][x + 1]
		if contains_mas(first) and contains_mas(second):
			xcount += 1

print(xcount)
