import re

regex = re.compile(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$")
n_correct_pwd = 0

with open("day2_input.txt") as file:
    for line in file:
        groups_p = re.match(regex, line)
        if groups_p is not None:
            min_n, max_n, char, pwd = groups_p.groups()
            min_n, max_n = int(min_n), int(max_n)
            if max_n >= pwd.count(char) >= min_n:
                n_correct_pwd += 1

print(n_correct_pwd)
