n, trees = 0, 0

with open("day3_input.txt") as file:
    for line in file:
        line = line.strip()
        if line[n] == "#":
            trees += 1
        n += 3
        if n > len(line) - 1:
            n -= len(line)

print(trees)
