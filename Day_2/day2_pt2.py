import re

regex = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$")
n_correct_pwd = 0

with open("day2_input.txt") as file:
    for line in file:
        groups_p = re.match(regex, line)
        if groups_p is not None:
            pos1, pos2, char, pwd = groups_p.groups()
            pos1, pos2 = int(pos1) - 1, int(pos2) - 1
            if (char == pwd[pos1]) ^ (char == pwd[pos2]):
                n_correct_pwd += 1

print(n_correct_pwd)
