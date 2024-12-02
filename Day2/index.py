import ast

with open('Day2/data.txt', 'r') as file:
    # Read each line and convert to an array of numbers
    data = [list(map(int, line.split())) for line in file]

result = 0

def check(arr: list[int]):
    if len(arr) < 2:
        return True

    for i in range(len(arr) - 1):
        gap = arr[i + 1] - arr[i]

        if(abs(gap) < 1 or abs(gap) > 3):
            return False
    
    isAscending = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    isDescending = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    return isAscending or isDescending

for line in data:
    if (check(line)):
        result += 1


print(result)