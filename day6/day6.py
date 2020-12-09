# Part 1
#
# with open("input.txt", "r") as file:
#     group_answers = file.read().split('\n\n')
#     sum_counts = 0
#     for answers in group_answers:
#         sum_counts += len({q for q in answers.replace('\n', '')})
#     print(sum_counts)

# Part 2

from collections import Counter

with open("input.txt", "r") as file:
    all_group_answers = file.read().split('\n\n')
    sum_counts = 0
    for group_answers in all_group_answers:
        group_size = group_answers.count('\n') + 1
        counts = Counter(group_answers.replace('\n', ''))
        for answer, occ in counts.items():
            if occ == group_size:
                sum_counts += 1

    print(sum_counts)
