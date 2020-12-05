import re

with open("input.txt", "r") as file:
    count_valid = 0
    for line in file.readlines():
        pattern = '(\d+)-(\d+) ([a-z]): ([a-z]+)'
        groups = re.search(pattern, line).groups()
        range_from = int(groups[0])
        range_to = int(groups[1])
        letter = groups[2]
        password = groups[3]
        # letter_occurrence = password.count(letter)
        # if letter_occurrence in range(range_from, range_to + 1):
        #    count_valid += 1
        if bool(password[range_from - 1] == letter) ^ bool(password[range_to - 1] == letter):
            count_valid += 1
    print(count_valid)
