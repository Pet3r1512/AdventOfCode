with open("Day4/data.txt", "r") as file:
    data = file.readlines()
# Define the pattern to match (req1)
req = [
    ["S", "_", "_", "S", "_", "A", "S"],
    ["_", "A", "_", "A", "_", "A", "_"],
    ["_", "_", "M", "M", "M", "_", "_"],
    ["S", "A", "M", "X", "M", "A", "S"],
    ["_", "_", "M", "M", "M", "_", "_"],
    ["_", "A", "_", "A", "_", "A", "_"],
    ["S", "_", "_", "S", "_", "A", "S"],
]

# Matrix dimensions
matrix = [list(line.strip()) for line in data]
count = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == "X":
            # right
            if x + 3 < len(matrix) and matrix[x+1][y] == "M" and matrix[x+2][y] == "A" and matrix[x+3][y] == "S":
                count += 1
            # left
            if x - 3 >= 0 and matrix[x-1][y] == "M" and matrix[x-2][y] == "A" and matrix[x-3][y] == "S":
                count += 1
            # top
            if y + 3 < len(matrix[x]) and matrix[x][y+1] == "M" and matrix[x][y+2] == "A" and matrix[x][y+3] == "S":
                count += 1
            # bottom
            if y - 3 >= 0 and matrix[x][y-1] == "M" and matrix[x][y-2] == "A" and matrix[x][y-3] == "S":
                count += 1
            # top-right
            if x + 3 < len(matrix) and y + 3 < len(matrix[x]) and matrix[x+1][y+1] == "M" and matrix[x+2][y+2] == "A" and matrix[x+3][y+3] == "S":
                count += 1
            # top-left
            if x - 3 >= 0 and y + 3 < len(matrix[x]) and matrix[x-1][y+1] == "M" and matrix[x-2][y+2] == "A" and matrix[x-3][y+3] == "S":
                count += 1
            # bottom-right
            if x + 3 < len(matrix) and y - 3 >= 0 and matrix[x+1][y-1] == "M" and matrix[x+2][y-2] == "A" and matrix[x+3][y-3] == "S":
                count += 1
            # bottom-left
            if x - 3 >= 0 and y - 3 >= 0 and matrix[x-1][y-1] == "M" and matrix[x-2][y-2] == "A" and matrix[x-3][y-3] == "S":
                count += 1
print("part1")
print(count)

count2 = 0
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if matrix[x][y] == "A":
            if (
                x + 1 < len(matrix) and y + 1 < len(matrix[0]) and
                x + 1 < len(matrix) and y - 1 >= 0 and
                x - 1 >= 0 and y + 1 < len(matrix[0]) and
                x - 1 >= 0 and y - 1 >= 0
            ):
                if matrix[x+1][y+1] == "S" and matrix[x+1][y-1] == "S" and matrix[x-1][y+1] == "M" and matrix[x-1][y-1] == "M":
                    count2 += 1
                if matrix[x+1][y+1] == "M" and matrix[x+1][y-1] == "M" and matrix[x-1][y+1] == "S" and matrix[x-1][y-1] == "S":
                    count2 += 1
                if matrix[x+1][y+1] == "M" and matrix[x+1][y-1] == "S" and matrix[x-1][y+1] == "M" and matrix[x-1][y-1] == "S":
                    count2 += 1
                if matrix[x+1][y+1] == "S" and matrix[x+1][y-1] == "M" and matrix[x-1][y+1] == "S" and matrix[x-1][y-1] == "M":
                    count2 += 1
print("part2")
print(count2)