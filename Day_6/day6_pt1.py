union_pos_answers = set()
sum_qs_answered = 0

with open("day6_input.txt") as file:
    for line in file:
        for answers in line.strip():
            pos_answers_set = set(answers)  # Set of answered questions
            union_pos_answers |= pos_answers_set
        if line == "\n":
            sum_qs_answered += len(union_pos_answers)
            union_pos_answers.clear()

print(sum_qs_answered)
