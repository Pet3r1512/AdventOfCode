with open("testdata.txt", "r") as file:
    # Read lines and split into two columns
    data = file.read().splitlines()
s = 50
r = 0

for line in data:
    direction = line[0]
    distance = int(line[1:])

    if s == 0:
        r += 1

    if direction == "L":
        s = (s - distance) % 100
    else:
        s = (s + distance) % 100

print(r)
    
    