with open("input.txt") as f:
	data = f.read().strip().split("\n\n")
rules = [list(map(int, line.split("|"))) for line in data[0].split("\n")]
updates = [list(map(int, line.split(","))) for line in data[1].split("\n")]

def update_passes_rules(update):
	print("Checking update: ", update)
	for rule in rules:
		# Check if the update complies to all the rules
		if (rule[0] in update and update.index(rule[0]) != len(update) - 1):
			if (rule[1] in update and not(rule[1] in update[update.index(rule[0]) + 1:])):
				print("Failed rule: ", rule)
				return False
	return True

total = 0
for update in updates:
	if (update_passes_rules(update)):
		print("Passed: ", update)
		to_add = update[len(update) // 2]
		print("Adding: ", to_add)
		total += to_add
print(total)
