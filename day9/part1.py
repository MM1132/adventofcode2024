with open("input.txt") as f:
	line = f.readline().strip()

storage = []
file_index = 0
for i, c in enumerate(line):
	# File
	if (i % 2 == 0):
		for i in range(int(c)):
			storage.append(str(file_index))
		file_index += 1
	# Free space
	else:
		for i in range(int(c)):
			storage.append('.')

# Compress
while ('.' in storage):
	free_space_index = storage.index('.')
	storage[free_space_index] = storage.pop()

# Checksum
checksum = sum([i * int(v) for i, v in enumerate(storage)])
print(checksum)

# Print storage
print("".join(storage))