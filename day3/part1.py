import re
with open('input.txt') as f:
    lines = f.readlines()
lines = "".join(lines)
total = 0
print(lines)
for v in re.finditer(r'mul\((\d+),(\d+)\)', lines):
    total += int(v.group(1)) * int(v.group(2))
print(total)
