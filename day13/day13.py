# Part 1

# import re
# import sys
#
# with open('input.txt', 'r') as file:
#     my_earliest_departure = int(file.readline())
#     bus_lines = [int(b) for b in re.findall('[0-9]+', file.readline())]
#     earliest_bus = 0
#     earliest_bus_departure = sys.maxsize
#     for bus in bus_lines:
#         t = 0
#         while t < my_earliest_departure:
#             t += bus
#         if t < earliest_bus_departure:
#             earliest_bus = bus
#             earliest_bus_departure = t
#     print(earliest_bus * (earliest_bus_departure - my_earliest_departure))
#

# Part 2

with open("input.txt", "r") as f:
    f = f.read().splitlines()

buses = [(int(b), i) for i, b in enumerate(f[1].split(",")) if b != "x"]

jump = i = buses[0][0]
for b in buses[1:]:
    while (i + b[1]) % b[0] != 0:
        i += jump
    jump *= b[0]

print(i)
