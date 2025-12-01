with open("Day1.txt", "r") as file:
    data = file.read().splitlines()

s = 50 
r = 0  

for line in data:
    direction = line[0]
    distance = int(line[1:])

    for i in range(distance):
        if direction == "R":
            s = (s + 1)%100
        else:
            s = (s - 1)%100
        
        if s == 0:
            r += 1

print(r)
