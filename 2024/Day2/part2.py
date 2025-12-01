import ast

with open('Day2/data.txt', 'r') as file:
    data = [list(map(int, line.split())) for line in file]

result = 0

def is_safe_report(line: list[int]) -> bool:
    if len(line) < 2:
        return True
    
    for i in range(len(line) - 1):
        gap = abs(line[i + 1] - line[i])
        if gap < 1 or gap > 3:
            return False
    
    is_ascending = line == sorted(line)
    is_descending = line == sorted(line, reverse=True)
    return is_ascending or is_descending

def dampener(line: list[int]) -> bool:
    if is_safe_report(line):
        return True
    
    # try to remove each element from the array and check is new array safe
    for i in range(len(line)):
        newLine = line.copy()
        newLine.pop(i)
        if is_safe_report(newLine):
            return True
    
    return False

result1 = 0
for line in data:
    if dampener(line):
        result1 += 1

print(result1)
