from collections import Counter 

# Read the file and process as two columns
with open("Day1/data.txt", "r") as file:
    # Read lines and split into two columns
    data = [line.split() for line in file.readlines()]

# Convert to integers if needed
data = [(int(col1), int(col2)) for col1, col2 in data]

# Print the data in two columns (left and right)
left = []
right = []

for col1, col2 in data:
    left.append(col1)
    right.append(col2)

left.sort()

col2_dic = Counter(right)
result = 0
for n in left:
    result += n * col2_dic[n]

print(result)
