# Part 1

# import re
#
# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#     memory = {}
#     setting_mask = 0
#     resetting_mask = 0
#     for line in lines:
#         if line[:7] == 'mask = ':
#             setting_mask = 0
#             resetting_mask = 0
#             i = 35
#             for b in line[7:]:
#                 if b == '0':
#                     resetting_mask += pow(2, i)
#                 elif b == '1':
#                     setting_mask += pow(2, i)
#                 i -= 1
#             resetting_mask = ~resetting_mask
#         else:
#             match = re.search('mem\[([0-9]+)\] = ([0-9]+)', line)
#             address = int(match.group(1))
#             value = int(match.group(2))
#             memory[address] = (value & resetting_mask) | setting_mask
#     print(sum(val for key, val in memory.items()))

# Part 2

import re


def mask_address(addr, floating_bits):
    addr_bin_reversed = (format(addr, '036b'))[::-1]
    new_addresses = []
    for x in range(pow(2, len(floating_bits))):
        na = addr_bin_reversed
        x_bin = format(x, '0' + str(len(floating_bits)) + 'b')
        for idx, bit in enumerate(floating_bits):
            na = na[:bit] + x_bin[idx] + na[bit+1:]
        new_addresses.append(int(na[::-1], 2))
    return new_addresses


with open('input.txt', 'r') as file:
    lines = file.readlines()
    memory = {}
    setting_mask = 0
    floating_mask = []
    for line in lines:
        if line[:7] == 'mask = ':
            setting_mask = 0
            floating_mask = []
            i = 35
            for b in line[7:]:
                if b == '1':
                    setting_mask += pow(2, i)
                elif b == 'X':
                    floating_mask.append(i)
                i -= 1
        else:
            match = re.search('mem\[([0-9]+)\] = ([0-9]+)', line)
            address = int(match.group(1))
            value = int(match.group(2))
            for a in mask_address(address | setting_mask, floating_mask):
                # print(a)
                memory[a] = value
            # print()
    print(sum(val for key, val in memory.items()))
