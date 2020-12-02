import itertools

with open("day1_input.txt") as file:
    inputs_list = [int(line.strip()) for line in file]

# First algorithm
# xy_sum = 0
# x, y = 0, 0
#
# while xy_sum != 2020:
#     if y == len(inputs_list) - 1:   # If y is the last number
#         x += 1
#         y = 0
#     else:
#         y += 1
#
#     xy_sum = inputs_list[x] + inputs_list[y]

# Better algorithm
for x, y in itertools.product(inputs_list, inputs_list):
    if x + y == 2020:
        xy = [x, y]
        xy_sum = x + y
        product = x * y
        print(f"{xy[0]} + {xy[1]} = {xy_sum}")
        print(f"{xy[0]} * {xy[1]} = {product}")
        break
