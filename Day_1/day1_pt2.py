import itertools

with open("day1_input.txt") as file:
    inputs_list = [int(line.strip()) for line in file]

# First algorithm
# xyz_sum = 0
# x, y, z = 0, 0, 0
#
# while xyz_sum != 2020:
#     if z == len(inputs_list) - 1:  # If z is the last number
#         z = 0
#         y += 1
#     if y == len(inputs_list) - 1:  # If y is the last number
#         y = 0
#         x += 1
#     else:
#         z += 1
#
#     xyz_sum = inputs_list[x] + inputs_list[y] + inputs_list[z]

# Better algorithm
for x, y, z in itertools.combinations(inputs_list, 3):
    if x + y + z == 2020:
        xyz_sum = x + y + z
        product = x * y * z
        print(f"{x} + {y} + {z} = {xyz_sum}")
        print(f"{x} * {y} * {z} = {product}")
        break
