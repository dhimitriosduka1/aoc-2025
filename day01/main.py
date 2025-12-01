import os

input_path = os.path.join(os.path.dirname(__file__), "input_part1.txt")
with open(input_path, "r") as file:
    rotations = [line.strip() for line in file.readlines()]

current_position = 50

# Part 1
count = 0
for rotation in rotations:
    direction = rotation[0]
    value = int(rotation[1:])

    if direction == "L":
        current_position = current_position - value
    elif direction == "R":
        current_position = current_position + value

    current_position %= 100
    
    if current_position == 0:
        count += 1

print("Password:", count)

# Part 2
input_path = os.path.join(os.path.dirname(__file__), "input_part2.txt")
with open(input_path, "r") as file:
    rotations = [line.strip() for line in file.readlines()]

current_position = 50
count = 0

for rotation in rotations:
    direction = rotation[0]
    value = int(rotation[1:])

    number_of_full_rotations = value // 100
    count += number_of_full_rotations

    remaining_rotation = value - (number_of_full_rotations * 100)

    assert remaining_rotation < 100

    distance_to_zero = (100 - current_position) if direction == "R" else current_position
    
    if remaining_rotation >= distance_to_zero and distance_to_zero != 0:
        count += 1

    if direction == "L":
        current_position = current_position - remaining_rotation
    elif direction == "R":
        current_position = current_position + remaining_rotation

    current_position %= 100

print("Password:", count)