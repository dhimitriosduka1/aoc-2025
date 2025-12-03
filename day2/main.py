import os

# Part 1
def is_invalid_id_part1(id):
    midpoint = len(id) // 2
    return id[:midpoint] == id[midpoint:]

input_path = os.path.join(os.path.dirname(__file__), "input_part1.txt")

result = 0
with open(input_path, "r") as file:
    ranges = [line.strip() for line in file.readlines()][0].split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if is_invalid_id_part1(str(i)):
                result += i

print(f"Final result part 1: {result}")

# Part 2
def is_invalid_id_part2(id):
    if len(id) > 1 and len(set(id)) == 1:
        return True
    
    initial = id[:2]
    count = id.count(initial)
    longest = initial
    for i in range(2, len(id) + 1):
        substring = id[:i]
        current_count = id.count(substring)
        if current_count >= count:
            count = current_count
            longest = substring

    if len(id) != count * len(longest):
        return False
        
    return count > 1

input_path = os.path.join(os.path.dirname(__file__), "input_part2.txt")

result = 0
invalid_ids = set()
with open(input_path, "r") as file:
    ranges = [line.strip() for line in file.readlines()][0].split(",")
    for r in ranges:
        start, end = r.split("-")
        for i in range(int(start), int(end) + 1):
            if is_invalid_id_part2(str(i)):
                invalid_ids.add(i)

print(f"Final result part 2: {sum(invalid_ids)}")