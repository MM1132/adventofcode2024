with open("input.txt") as f:
	line = f.readline().strip()

def find_first_free_space_index_of_length(storage, length):
	for i, v in enumerate(storage):
		if (v == '.'):
			free_space_characters = [storage[i + j] for j in range(length) if i + j < len(storage)]
			# print(free_space_characters)
			
			all_are_free = all([char == '.' for char in free_space_characters])
			# print(all_are_free)

			if (all_are_free and len(free_space_characters) == length):
				return i
	return -1

def get_file_location(storage, file_index):
	location = 0
	while location < len(storage):
		if storage[location] == file_index:
			return location
		location += 1
	return -1

def get_length_of_file(storage, file_index):
	length = 0
	for char in storage:
		if char == file_index:
			length += 1
	return length

def solve():
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

	# print(storage)
	# free_space_index = find_first_free_space_index_of_length(storage, 4)
	# print(free_space_index)
	# exit()

	# Move left
	for file_index in range(file_index - 1, -1, -1):
		file_index = str(file_index)

		file_location = get_file_location(storage, file_index)
		file_length = get_length_of_file(storage, file_index)

		free_space_index = find_first_free_space_index_of_length(storage, file_length)
		if (free_space_index == -1 or free_space_index >= file_location):
			continue

		# print("Placing...")
		# print("Index", file_index)
		# print("location:", file_location)
		# print("Length", file_length)
		# print(storage)
		# exit()

		# print("Found free space for", file_length, "at", free_space_index)

		for i in range(file_length):
			storage[free_space_index + i], storage[file_location + i] = storage[file_location + i], storage[free_space_index + i]
		# print("".join(storage))
	
	# print(storage)

	# Compress
	# while ('.' in storage):
	# 	free_space_index = storage.index('.')
	# 	storage[free_space_index] = storage.pop()

	# Checksum
	checksum = sum([i * int(v) for i, v in enumerate(storage) if v != '.'])
	print(checksum)

solve()

# Print storage
# print("".join(storage))
