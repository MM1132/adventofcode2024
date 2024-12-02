with open("input.txt") as f:
	lines = f.readlines()
	reports = [[int(v) for v in line.split(" ")] for line in lines]
def is_safe(report):
	if not (sorted(report) == report or list(reversed(sorted(report))) == report):
		return False
	for index in range(len(report) - 1):
		distance = abs(report[index] - report[index + 1])
		if (distance > 3 or distance == 0):
			break
		if (index == len(report) - 2):
			return True
		print("\n")
total = 0
for report in reports:
	if (is_safe(report)):
		total += 1
		continue
	# Check the Problem Dampener
	for index in range(len(report)):
		report_copy = report[:]
		report_copy.pop(index)
		if is_safe(report_copy):
			total += 1
			break
print(total)
