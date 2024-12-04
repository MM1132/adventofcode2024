import re
with open('input.txt') as f:
    lines = f.readlines()
lines = "".join(lines)
total = 0
counting = True
for v in re.finditer(r"(mul\((\d+),(\d+)\))|don't\(\)|do\(\)", lines):
    if v.group(0) == "don't()":
        counting = False
    elif v.group(0) == "do()":
        counting = True
    elif counting:
        total += int(v.group(2)) * int(v.group(3))
print(total)
