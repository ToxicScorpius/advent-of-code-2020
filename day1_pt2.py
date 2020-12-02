inputs_list = []

with open("day1_input.txt") as file:
    for line in file:
        line = int(line.strip())
        inputs_list.append(line)

xyz_sum = 0
x, y, z = 0, 0, 0

while xyz_sum != 2020:
    if z == len(inputs_list) - 1:  # If z is the last number
        z = 0
        y += 1
    if y == len(inputs_list) - 1:  # If y is the last number
        y = 0
        x += 1
    else:
        z += 1

    xyz_sum = inputs_list[x] + inputs_list[y] + inputs_list[z]

product = inputs_list[x] * inputs_list[y] * inputs_list[z]
print(f"{inputs_list[x]} + {inputs_list[y]} + {inputs_list[z]} = {xyz_sum}")
print(f"{inputs_list[x]} * {inputs_list[y]} * {inputs_list[z]} = {product}")
