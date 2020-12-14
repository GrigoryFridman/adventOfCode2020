# Part 1

# with open('input.txt', 'r') as file:
#     adapters = [int(a) for a in file.read().split('\n')]
#     adapters.sort()
#     one_jolt_diffs = 0
#     three_jolt_diffs = 1
#     current_jolt = 0
#     for out_jolt in adapters:
#         if out_jolt - current_jolt == 1:
#             one_jolt_diffs += 1
#         elif out_jolt - current_jolt == 3:
#             three_jolt_diffs += 1
#         current_jolt = out_jolt
#     print(one_jolt_diffs * three_jolt_diffs)

# Part 2

with open('input.txt', 'r') as file:

    adapters = sorted([0] + [int(a) for a in file.read().split('\n')])
    highest_adapter = max(adapters)
    adapters += [highest_adapter + 3]
    adapters_with_links = {a: 1 for a in adapters}
    for i, a in enumerate(adapters):
        for j in (i + 2, i + 3):
            if j < len(adapters) and adapters[j] - a <= 3:
                for a_next in adapters[j:]:
                    adapters_with_links[a_next] += adapters_with_links[a]
    print(adapters_with_links[highest_adapter])
