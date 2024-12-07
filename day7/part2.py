class Equation:
	def __init__(self, answer, numbers):
		self.answer = answer
		self.numbers = numbers

with open("input.txt") as f:
	lines = f.read().strip()
	lines = lines.split("\n")

lines = [[v.strip() for v in line.split(":")] for line in lines]
equations = [Equation(int(line[0]), list(map(int, line[1].split()))) for line in lines]

def check_equation(equation, operators):

	if len(operators) != len(equation.numbers) - 1:
		return False

	answer = equation.numbers[0]
	for index in range(len(operators)):
		if operators[index] == '+':
			answer += equation.numbers[index + 1]
		elif operators[index] == '*':
			answer *= equation.numbers[index + 1]
		elif operators[index] == '|':
			answer = int(str(answer) + str(equation.numbers[index + 1]))

	is_solvable = answer == equation.answer
	# if (is_solvable):
	# 	print(equation.answer, ":", equation.numbers, ":", operators)
	return is_solvable

def is_solvable(equation, operators):
	if len(operators) >= len(equation.numbers):
		return False
	if check_equation(equation, operators):
		return True
	return is_solvable(equation, operators + '|') or is_solvable(equation, operators + "+") or is_solvable(equation, operators + "*")

total = 0
for equation in equations:
	if (is_solvable(equation, "")):
		total += equation.answer
print(total)
