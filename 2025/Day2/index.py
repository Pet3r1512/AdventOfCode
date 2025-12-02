with open("data.txt", "r") as file:
    data = file.read()

# part 1

def check(s):
    if len(s) % 2 != 0:
        return False
    
    if s[0] == '0':
        return False
    
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    return first_half == second_half

total = 0
ranges = data.split(",")

for range_str in ranges: 
    s, e = range_str.split("-")[0], range_str.split("-")[1]
    for step in range(int(s), int(e) + 1):
        if check(str(step)):
            total += step

print(total)



# Part 2
def check2(s):
    if s[0] == "0":
        return False

    for pattern_len in range(1, len(s) // 2 + 1):
        if len(s) % pattern_len == 0:
            pattern = s[:pattern_len]
            # repeat the pattern until = len(s), then compare it to s
            if pattern * (len(s) // pattern_len) == s:
                return True
            
    return False

total2 = 0

for range_str in ranges: 
    s, e = range_str.split("-")[0], range_str.split("-")[1]
    for step in range(int(s), int(e) + 1):
        if check2(str(step)):
            total2 += step

print(total2)