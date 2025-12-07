import os


# Part 1
def compute_max_jolatage(bank):
    max_jolatage = -1
    for i in range(0, len(bank) - 1):
        for j in range(i + 1, len(bank)):
            jolatage = int(str(bank[i]) + str(bank[j]))
            if jolatage > max_jolatage:
                max_jolatage = jolatage

    return max_jolatage


max_jolateges = []
with open(os.path.join(os.path.dirname(__file__), "input_part1.txt")) as f:
    input_data = f.read().strip().splitlines()
    for bank in input_data:
        jolatages = list(map(int, bank))
        max_jolateges.append(compute_max_jolatage(jolatages))

print("Part 1:", sum(max_jolateges))

# Part 2
with open(os.path.join(os.path.dirname(__file__), "input_part2.txt")) as f:
    input_data = f.read().strip().splitlines()
    print(input_data)