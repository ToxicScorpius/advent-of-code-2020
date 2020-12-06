from day5_function import find_id

ID, highest_ID = 0, 0
with open("day5_input.txt") as file:
    lines = [line.strip() for line in file]
    for line in lines:
        new_ID = find_id(line)
        highest_ID = max(highest_ID, new_ID)

print(highest_ID)
