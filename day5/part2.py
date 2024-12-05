with open("input.txt") as f:
	data = f.read().strip().split("\n\n")
rules = [list(map(int, line.split("|"))) for line in data[0].split("\n")]
updates = [list(map(int, line.split(","))) for line in data[1].split("\n")]

def update_passes_rules(update):
	for rule in rules:
		# Check if the update complies to all the rules
		if (rule[0] in update and update.index(rule[0]) != len(update) - 1):
			if (rule[1] in update and not(rule[1] in update[update.index(rule[0]) + 1:])):
				return False
	return True

def find_rules_for_update(update):
	return [rule for rule in rules if rule[0] in update and rule[1] in update]

def as_sorted_update(update, rules):
	print("Was not ordered:", update)
	new_update = update[:]
	for i in range(len(new_update) - 1):
		for j in range(i + 1, len(new_update)):
			for rule in rules:
				if new_update[i] == rule[1]:
					if new_update[j] == rule[0]:
						new_update[i], new_update[j] = new_update[j], new_update[i]
	print("Is now ordered:", new_update)
	return new_update

total = 0
for update in updates:
	rules_for_update = find_rules_for_update(update)
	if update_passes_rules(update):
		continue
	sorted_update = as_sorted_update(update, rules_for_update)
	to_add = sorted_update[len(sorted_update) // 2]
	total += to_add
print(total)