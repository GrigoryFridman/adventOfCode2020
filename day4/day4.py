import re

field_conditions = {'byr': lambda val: 1920 <= int(val) <= 2002,
                    'iyr': lambda val: 2010 <= int(val) <= 2020,
                    'eyr': lambda val: 2020 <= int(val) <= 2030,
                    'hgt': lambda val: re.search('^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$', val),
                    'hcl': lambda val: re.search('^#([a-f]|[0-9]){6}$', val),
                    'ecl': lambda val: val in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
                    'pid': lambda val: re.search('^[0-9]{9}$', val)}


def check_passport(f):
    for field, condition in field_conditions.items():
        if field not in f or not condition(f[field]):
            return False
    return True


with open("input.txt", "r") as file:
    passports = file.read().split('\n\n')
    valid = 0
    for passport in passports:
        fields = {match.group(1): match.group(2) for match in re.finditer('([a-z]{3}):(.[^\s]+)', passport)}
        if check_passport(fields):
            valid += 1
    print(valid)
