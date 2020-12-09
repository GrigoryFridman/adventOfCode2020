import re

# Part 1
#
# def find_all_outer_bags(inner_bag, all_incs, outer_bags):
#     for outer, incs in all_incs.items():
#         if inner_bag in incs:
#             outer_bags.add(outer)
#             find_all_outer_bags(outer, all_incs, outer_bags)
#
#
# with open("input.txt", "r") as file:
#     all_rules = file.readlines()
#     bag_includes = {}
#     for rule in all_rules:
#         match = re.search('(\w+ \w+) bags contain (.*)', rule)
#         bag_includes[match.group(1)] = [c.group(1) for c in re.finditer('\d (\w+ \w+) bags?', match.group(2))]
#
#     colors_inc_shiny_gold = set()
#     find_all_outer_bags('shiny gold', bag_includes, colors_inc_shiny_gold)
#
#     print(colors_inc_shiny_gold)
#     print(len(colors_inc_shiny_gold))

# Part 2


def count_sum_inner_bags(outer, all_incs):
    sum_inner_bags = 0
    outer_incs = all_incs[outer]
    for inc, cnt in outer_incs.items():
        sum_inner_bags += cnt + cnt * count_sum_inner_bags(inc, all_incs)
    return sum_inner_bags


with open("input.txt", "r") as file:
    ruleset = file.readlines()
    bag_includes = {}
    for rule in ruleset:
        match = re.search('(\w+ \w+) bags contain (.*)', rule)
        bag_includes[match.group(1)] = {c.group(2): int(c.group(1)) for c in re.finditer('(\d) (\w+ \w+) bags?', match.group(2))}

    count = count_sum_inner_bags('shiny gold', bag_includes)
    print(count)
