def check_trees(steps_right, steps_down):
    """
    Check whether there is a tree on index [n], increment the tree count
    and reset the line if necessary, then return the tree count.
    """
    lines = [line.strip() for line in open("day3_input.txt")]
    trees_count, index, line_count = 0, 0, 0
    for line in lines:
        if line_count % steps_down == 0:
            if line[index] == "#":
                trees_count += 1
            index += steps_right
            if index > len(line) - 1:
                index -= len(line)
        line_count += 1
    return trees_count
