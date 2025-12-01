import re
# Read the contents of the file
with open("Day3/data.txt", "r") as file:
    data = file.read().replace("\r", "").strip()

def calculate(mul_str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    match = re.search(pattern, mul_str)
    
    if match:
        x = int(match.group(1))
        y = int(match.group(2))
        print("valid", mul_str)
        return x * y
    return 0

result = 0
enabled = True

def check_do(data):
    global enabled
    global result
    pattern = r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))'
    
    matches = re.findall(pattern, data)

    for match in matches:
        if match[0]:
            mul_str = match[0]
            if enabled:
                result += calculate(mul_str)
        elif match[1]:
            enabled = True
        elif match[2]:
            enabled = False

# Process the data
check_do(data)

for line in data:
    check_do(line)

# 127092535  
print(result)