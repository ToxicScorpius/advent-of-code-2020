n1, n2, n3, n4, n5 = 0, 0, 0, 0, 0
s1_trees, s2_trees, s3_trees, s4_trees, s5_trees = 0, 0, 0, 0, 0
line_count = 0

with open("day3_input.txt") as file:
    for line in file:
        line = line.strip()
        if line[n1] == "#":
            s1_trees += 1
        if line[n2] == "#":
            s2_trees += 1
        if line[n3] == "#":
            s3_trees += 1
        if line[n4] == "#":
            s4_trees += 1
        if line_count % 2 == 0:
            if line[n5] == "#":
                s5_trees += 1

        n1 += 1
        n2 += 3
        n3 += 5
        n4 += 7
        if line_count % 2 == 0:
            n5 += 1

        if n1 > len(line) - 1:
            n1 -= len(line)
        if n2 > len(line) - 1:
            n2 -= len(line)
        if n3 > len(line) - 1:
            n3 -= len(line)
        if n4 > len(line) - 1:
            n4 -= len(line)
        if n5 > len(line) - 1:
            n5 -= len(line)

        line_count += 1
product = s1_trees * s2_trees * s3_trees * s4_trees * s5_trees


class ProductValidity(Exception):
    """Checks the validity of the product."""


try:
    if product != 6708199680:
        raise ProductValidity()
except ProductValidity:
    print(f"{product} != 6708199680")
    print("Invalid product.")

if product == 6708199680:
    print(f"{s1_trees}*{s2_trees}*{s3_trees}*{s4_trees}*{s5_trees} = {product}")
