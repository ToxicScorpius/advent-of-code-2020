inputs_list = []

with open("input.txt") as file:
    for line in file:
        line = int(line.strip())
        inputs_list.append(line)

xy_sum = 0
x, y = 0, 0

while xy_sum != 2020:
    if y == len(inputs_list) - 1:   # If y is the last number
        x += 1
        y = 0
    else:
        y += 1

    xy_sum = inputs_list[x] + inputs_list[y]

product = inputs_list[x] * inputs_list[y]
print(f"{inputs_list[x]} + {inputs_list[y]} = {xy_sum}")
print(f"{inputs_list[x]} * {inputs_list[y]} = {product}")
