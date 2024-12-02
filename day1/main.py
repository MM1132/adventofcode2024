with open("input.txt") as f:
	lines = f.readlines()
	list1 = [int(line.split("   ")[0]) for line in lines]
	list2 = [int(line.split("   ")[1]) for line in lines]	
total = 0
for i in range(len(list1)):
	occcurances = list2.count(list1[i])
	total += list1[i] * occcurances
print(total)