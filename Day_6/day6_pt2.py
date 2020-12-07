common_answers = set("abcdefghijklmnopqrstuvwxyz")
sum_common_answers = 0

with open("day6_input.txt") as file:
    for line in file:
        if line != "\n":
            pos_answers_set = set(line.strip())  # Set of answered questions
            common_answers &= pos_answers_set
        if line == "\n":
            sum_common_answers += len(common_answers)
            common_answers = set("abcdefghijklmnopqrstuvwxyz")

print(sum_common_answers)