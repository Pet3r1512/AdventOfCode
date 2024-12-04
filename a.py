import re

with open("Day3/data.txt", "r") as file:
    data = file.read().replace("\r", "").strip()

p1 = 0
p2 = 0
enabled = True
for i in range(len(data)):
    if data[i:].startswith('do()'):
        enabled = True
    if data[i:].startswith("don't()"):
        enabled = False
    instr = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', data[i:])
    if instr is not None:
        x,y = int(instr.group(1)), int(instr.group(2))
        p1 += x*y
        if enabled:
            p2 += x*y

print(p2)