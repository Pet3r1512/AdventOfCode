def move_target(matrix):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    turn_right = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    visited = set()  # To track visited positions
    target_position = None
    target_direction = None

    # Locate the target's initial position and direction
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell in directions:
                target_position = (i, j)
                target_direction = cell
                break
        if target_position:
            break

    current_row, current_col = target_position

    while True:
        # Determine the direction and calculate the farthest position until blocked
        delta_row, delta_col = directions[target_direction]
        next_row, next_col = current_row + delta_row, current_col + delta_col

        # Track all positions along the way until the obstacle or edge
        while (
            0 <= next_row < rows and
            0 <= next_col < cols and
            matrix[next_row][next_col] != '#'
        ):
            current_row, current_col = next_row, next_col
            next_row, next_col = current_row + delta_row, current_col + delta_col

        # Add all positions from the initial target position to the last valid position
        step_row, step_col = directions[target_direction]
        temp_row, temp_col = target_position
        while (temp_row, temp_col) != (current_row, current_col):
            visited.add((temp_row, temp_col))
            temp_row += step_row
            temp_col += step_col
        visited.add((current_row, current_col))  # Include the last valid position

        # Check the right direction
        right_direction = turn_right[target_direction]
        right_delta_row, right_delta_col = directions[right_direction]
        right_row, right_col = current_row + right_delta_row, current_col + right_delta_col

        # Stop if both forward and right are blocked
        if (
            right_row < 0 or right_row >= rows or
            right_col < 0 or right_col >= cols or
            matrix[right_row][right_col] == '#'
        ):
            break

        # Otherwise, turn right
        target_direction = right_direction
        target_position = (current_row, current_col)  # Update target position

    return len(visited)

def read_data_as_2d_array(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

file_path = 'Day6/data.txt'
data_array = read_data_as_2d_array(file_path)

steps = move_target(data_array)
print("Steps moved:", steps)
